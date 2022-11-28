from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from firebase_admin import credentials, db, storage
from PythonSed import Sed, SedException
from datetime import datetime
from dateutil.relativedelta import relativedelta

import base64
import uvicorn
import json
import os
import firebase_admin
import requests
import subprocess

from featureVectorConverter import *
from classifierGenerator import *

origins = [
    "http://indoor.jonascsantos.com",
    "https://indoor.jonascsantos.com",
    "http://localhost:8080"
]

class Item(BaseModel):
    scanSamples: str
    sensorId: str

if os.getenv("SERVICE_ACCOUNT_KEY"):
    serviceAccountKey = os.getenv("SERVICE_ACCOUNT_KEY")

    decodeBase64 = base64.b64decode(serviceAccountKey)
    serviceAccountKey = decodeBase64.decode("ascii") 

    with open("serviceAccountKey.json", "w") as f:
        print(serviceAccountKey, file=f)
    
    cred = credentials.Certificate('serviceAccountKey.json')

    if os.getenv("FIREBASE_HOST_ENV") and os.getenv("FIREBASE_STORAGE_BUCKET_ENV") :
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://' + os.getenv("FIREBASE_HOST_ENV"),
            'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET_ENV")
        })

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"server_info": "Indoor Positioning Azure API"}

@app.post("/ai-generate/")
def create_item(item: Item):
    item_dict = item.dict()
    scanSamples = json.loads(item.scanSamples)
    sensorId = item.sensorId
    
    str1 = " "
    str1 = str1.join(scanSamples)

    with open("scanSamples.txt", "w") as f:
        print(str1, file=f)
    
    ref = db.reference("/" + sensorId + "/FIRMWARE/" )
    inoFileUrl = ref.child('WifiScanIno/url').get()
    if inoFileUrl is None:
        ref = db.reference("/")
        inoFileUrl = ref.child('StandardArduinoFile').get()


    r = requests.get(inoFileUrl, allow_redirects=True)
    open('firmware.ino', 'wb').write(r.content)

    if os.getenv("FIREBASE_HOST_ENV") and os.getenv("FIREBASE_AUTH_ENV"):
        print("SED RUNNING")
        try:
            sed = Sed()
            strCred = "s/FIREBASE_HOST_ENV/" + os.getenv("FIREBASE_HOST_ENV") + "/\ns/FIREBASE_AUTH_ENV/" + os.getenv("FIREBASE_AUTH_ENV") +"/"
            strAppend = '\n/^#endif.*/a \\n#include "Converter.h"\\n#include "Classifier.h"\\n\\nEloquent::Projects::WifiIndoorPositioning positioning;\\nEloquent::ML::Port::DecisionTree classifier;'
            strFunc= '\n/delay(2);.*/i \\nif(!isScanning && isTrackPositionOn()) {\\r\\n      positioning.scan();\\r\\n\\r\\n      location = classifier.predictLabel(positioning.features);\\r\\n   \\r\\n      jsonPositioning.set(\"room\", location);\\r\\n      jsonPositioning.set(\"Ts\/.sv\", \"timestamp\");\\r\\n\\r\\n      if (Firebase.RTDB.pushJSON(&fbdo, \"\/\" + hostString + \"\/TRACK_POSITION\/ROOM\", &jsonPositioning)) {\\r\\n          Serial.println(fbdo.dataPath());\\r\\n          Serial.println(fbdo.pushName());\\r\\n          Serial.println(fbdo.dataPath() + \"\/\"+ fbdo.pushName());\\r\\n      } else {\\r\\n          Serial.println(fbdo.errorReason());\\r\\n      }     \\r\\n    }'

            with open("script.sed", "w") as f:
                print(strCred + strAppend + strFunc, file=f)

            sed.load_script('script.sed')
            sed.apply('firmware.ino', 'fastapi-app.ino')
            os.remove('firmware.ino')
        except SedException as e:
            print(e.message)
        except:
            raise 

    featureVectorConverter()
    classifierGenerator()

    print("compiling...")
    subprocess.run("/fastapi-app/bin/arduino-cli compile --output-dir /fastapi-app -b esp32:esp32:esp32 fastapi-app.ino", shell=True)

    fileName = "fastapi-app.ino.bin"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.chunk_size = 5 * 1024 * 1024

    print("Blob created. Uploading file:")
    
    blob.upload_from_filename(fileName)
    
    ini_time_for_now = datetime.now()
    expiration_time = ini_time_for_now + relativedelta(years=2)

    url = blob.generate_signed_url(expiration=expiration_time)

    print("fileUrl: " + url)

    ref = db.reference("/" + sensorId + "/FIRMWARE/WifiScan" )

    dbFirmwareFilename = ref.child('filename').get()
    dbFirmwareVersion = ref.child('version').get()

    if dbFirmwareFilename == fileName:
        dbFirmwareVersion = str(int(dbFirmwareVersion) + 1)
    else:
        dbFirmwareFilename = fileName
        dbFirmwareVersion = "1"

    metadata = {
        "filename": dbFirmwareFilename,
        "url": url,
        "version": dbFirmwareVersion
    }

    ref.update(metadata)

    print("DB Firmware Metadata was Updated")

    return metadata

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)