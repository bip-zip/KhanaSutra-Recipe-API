from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
index_page_router = APIRouter()


@index_page_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})
	