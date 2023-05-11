from fastapi import FastAPI
from core.config import settings
from apis.base import api_router

# including router
def include_router(app):
	app.include_router(api_router)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	return app 




app = start_application()

# crazy people who thinks of changing the world actually change the world.