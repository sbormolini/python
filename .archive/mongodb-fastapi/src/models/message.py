from pydantic import BaseModel

# Message class defined in Pydantic
class Message(BaseModel):
    channel: str
    author: str
    text: str