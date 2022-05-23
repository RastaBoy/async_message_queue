from uuid import uuid4

from .dto import Message


class AgentTask():
    def __init__(self, msg : Message):
        self.id = str(uuid4())
        self.msg = msg
    
    
    def task_info(self):
        return f"{self.id} -- {self.msg.title} -- {self.msg.text}"