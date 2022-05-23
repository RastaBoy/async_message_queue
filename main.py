import asyncio

from server import build_app, run_server
from rabbit_offline.publisher import Publisher

if __name__ == '__main__':
    publisher = Publisher()
    asyncio.run(run_server(build_app()))

