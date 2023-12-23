"""Main driver script."""
from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine
from fastapi import FastAPI


def include_router(app) -> None:
    """function to include api router to the app"""
    app.include_router(api_router)


def create_tables() -> None:
    """function to create all database table."""
    Base.metadata.create_all(bind=engine)


def start_application():
    """Function to start application."""
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PORJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    """root api function."""
    return {"msg": "Hello FastAPI"}
