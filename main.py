from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from firebase_admin import credentials, db, storage
from PythonSed import Sed, SedException

import uvicorn
import json
import os
import firebase_admin
import requests
import fileinput
import re

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

sed = Sed()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

cred = credentials.Certificate('/fastapi-app/serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flowsensor-bfbed.firebaseio.com'
})

@app.get("/")
def read_root():
    return {"server_info": "Indoor Positioning Azure API"}

@app.post("/ai-generate/")
async def create_item(item: Item):
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

    
    # dictionary = {
    #     "version":"testentry"
    # }

    # ref.child('WifiScanIno').update(dictionary)


    return item_dict

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)