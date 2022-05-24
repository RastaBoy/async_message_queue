from quart import Blueprint, request
from functools import wraps

from rabbit_offline.publisher import Publisher
from rabbit_offline.dto import Message
from rabbit_offline.types import AgentTask

api_bp = Blueprint('api_bp', __name__)

def api_result(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):

        return {
            'result': True,
            'data': await func(*args, **kwargs)
        }

    return wrapper


@api_bp.post('/create_test_task')
@api_result
async def create_test_task():
    data = await request.json
    if data.get('agent_id'):
        await Publisher().send_to(data.get('agent_id'), AgentTask(Message(title="Test Task", text="Hello World!")))
        return 'done'


@api_bp.post('/create_task')
@api_result
async def create_task():
    # По-хорошему должна быть валидация входящих данных
    data = await request.json
    if data.get('agent_id'):
        id = data.get('agent_id')
        if data.get('msg'):
            msg = Message(title=data['msg']['title'], text=data['msg']['text'])
            await Publisher().send_to(id, AgentTask(msg))
            return 'done'


@api_bp.post('/get_message')
@api_result
async def get_message():
    data = await request.json
    id = data.get('agent_id')
    if id:
        msg = await Publisher().get_message(id)
        return msg.to_json()


@api_bp.get('/register_agent')
@api_result
async def register_agent():
    return Publisher().create_agent_controller()