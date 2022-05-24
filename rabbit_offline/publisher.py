
from typing import List

from .types import AgentTask
from .agent_controller import AgentController


class Publisher:
    __agents : List[AgentController] = list()

    def __init__(self):
        ...


    def create_agent_controller(self):
        agent_controller = AgentController()
        self.__agents.append(agent_controller)
        return agent_controller.id


    def add_agent_controller(self, agent_controller : AgentController):
        self.__agents.append(agent_controller)
        return 


    async def get_message(self, id : str) -> AgentTask:
        for agent in self.__agents:
            if agent.id == id:
                return await agent.get_task()


    async def send_to(self, id: str, task : AgentTask):
        for agent in self.__agents:
            if agent.id == id:
                await agent.push_task(task)


    async def send_all(self, task : AgentTask):
        for agent in self.__agents:
            await agent.push_task(task)


    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
    
        return cls._instance




    