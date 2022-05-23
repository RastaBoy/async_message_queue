
from typing import List

from .types import AgentTask
from .agent_controller import AgentController


class Publisher:

    def __init__(self):
        self.agents : List[AgentController] = list()


    def create_agent_controller(self):
        agent_controller = AgentController()
        self.agents.append(agent_controller)
        return agent_controller.id


    def add_agent_controller(self, agent_controller : AgentController):
        self.agents.append(agent_controller)
        return 


    async def get_message(self, id : str):
        for agent in self.agents:
            if agent.id == id:
                return await agent.get_task()


    async def send_to(self, id: str, task : AgentTask):
        for agent in self.agents:
            if agent.id == id:
                agent.push_task(task)


    async def send_all(self, task : AgentTask):
        for agent in self.agents:
            agent.push_task(task)


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Publisher, cls).__new__(cls)
        return cls.instance




    