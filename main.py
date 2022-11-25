from typing import Union

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import uvicorn

import json

import os

from featureVectorConverter import *
from classifierGenerator import *

origins = [
    "http://indoor.jonascsantos.com",
    "https://indoor.jonascsantos.com",
    "http://localhost:8080"
]

class Item(BaseModel):
    scanSamples: str

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
async def create_item(item: Item):
    item_dict = item.dict()
    scanSamples = json.loads(item.scanSamples)

    str1 = " "
    str1 = str1.join(scanSamples)

    item_dict.update({"scanSamples": str1})

    with open("scanSamples.txt", "w") as f:
        print(str1, file=f)

    print(os.getenv("FIREBASE_HOST_ENV"))

    featureVectorConverter()
    classifierGenerator()

    return item_dict

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)