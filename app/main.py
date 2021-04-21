from fastapi import FastAPI
from .controllers import v1

def get_app():
    app = FastAPI(title="API Demo")
    app.include_router(
        v1.router,
        prefix="/api/v1"
    )
    return app