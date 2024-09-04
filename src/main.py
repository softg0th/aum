import asyncio
import os
import sys

import uvicorn
from fastapi import FastAPI
from api.v1.router import auth, chat

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')


def get_app() -> FastAPI:
    app = FastAPI()
    return app


app = get_app()
app.include_router(auth.router)
app.include_router(chat.router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8030)
