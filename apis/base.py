from fastapi import APIRouter
from apis.version1 import index_template


api_router = APIRouter()
api_router.include_router(index_template.index_page_router,prefix="",tags=["index_page"])
