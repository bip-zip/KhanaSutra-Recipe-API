from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})



