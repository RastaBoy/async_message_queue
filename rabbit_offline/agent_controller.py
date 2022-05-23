from uuid import uuid4

from asyncio.queues import Queue

from .types import AgentTask

class AgentController:
    def __init__(self):
        self.__id =  str(uuid4())
        self.__storage = Queue()

    @property
    def id(self):
        return self.__id

    @property
    def storage(self):
        return self.__storage

    
    async def push_task(self, task : AgentTask):
        await self.__storage.put(task)


    async def get_task(self):
        return await self.__storage.get()
    
