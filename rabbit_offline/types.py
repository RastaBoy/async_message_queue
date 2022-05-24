from uuid import uuid4

from .dto import Message
from .abc import Serializable

class AgentTask(Serializable):
    def __init__(self, msg : Message):
        self.id = str(uuid4())
        self.msg = msg

    def __str__(self):
        return f"{self.id} -- {self.msg.title} -- {self.msg.text}"


    def __dict__(self):
        return {
            'id' : self.id,
            'msg' : self.msg.serialize()
        }