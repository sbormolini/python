import os
import uvicorn

from typing import List
from pymongo import MongoClient
from fastapi import FastAPI, status

from models.message import Message



# mongo db configuration
#SERVER = "mongodb://127.0.0.1:27017"
#SERVER = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
SERVER = "mongodb://" + os.environ['MONGODB_HOSTNAME'] + ":27017/"
DB = "slack"
MSG_COLLECTION = "messages"


# Instantiate the FastAPI
app = FastAPI()

# load environment variables
port = os.environ["PORT"]
#port = 5000

@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return {"status": "running"}


@app.get("/channels", response_model=List[str])
def get_channels():
    """Get all channels in list form."""
    with MongoClient(SERVER) as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("channel")
        return distinct_channel_list


@app.get("/messages/{channel}", response_model=List[Message])
def get_messages(channel: str):
    """Get all messages for the specified channel."""
    with MongoClient(SERVER) as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"channel": channel})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(Message(**msg))
        return response_msg_list


@app.post("/post_message", status_code=status.HTTP_201_CREATED)
def post_message(message: Message):
    """Post a new message to the specified channel."""
    with MongoClient(SERVER) as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False, log_level="info")