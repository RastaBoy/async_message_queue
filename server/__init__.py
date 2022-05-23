from quart import Quart

from hypercorn.asyncio import serve
from hypercorn import Config as HyperCfg

from .api import api_bp

def build_app():
    app = Quart(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app


async def run_server(app: Quart):
    cfg = HyperCfg()
    cfg.bind = f'0.0.0.0:{5000}'
    return await serve(app, cfg)