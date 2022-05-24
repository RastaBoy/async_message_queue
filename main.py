import asyncio

from server import build_app, run_server
from rabbit_offline.publisher import Publisher
from rabbit_offline.dto import Message

if __name__ == '__main__':
    publisher = Publisher()
    msg = Message(title='temp', text='one')

    msg.serialize()

    asyncio.run(run_server(build_app()))

