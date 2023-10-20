import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import db
from app.controllers import auth, content

origins= [
    "http://localhost:3000"
]
def init_app():

    app = FastAPI(
        title= "Farmasi-app",
        description= "Management drugs",
        version= "1"
    )

    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=origins,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"]
    # )

    # @app.on_event("startup")
    # async def starup():
    #     db.init()

    app.include_router(auth.router,tags=['Drugs'],prefix='/api/drug')

    return app

app = init_app()

def start():
    """Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)