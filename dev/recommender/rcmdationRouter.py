from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")
rcmdation_router = APIRouter()

@rcmdation_router.get("/recommender", response_class=HTMLResponse)
async def get_recommendations_page(request: Request):
    return templates.TemplateResponse("recommender.html", {"request": request})

