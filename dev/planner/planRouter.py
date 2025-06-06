from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

plan_router = APIRouter()

templates = Jinja2Templates(directory="templates")

@plan_router.get("/planner", response_class=HTMLResponse)
async def get_planner_page(request: Request):
    return templates.TemplateResponse("planner.html", {"request": request})

@plan_router.post("/planner", response_class=HTMLResponse)
async def plan_page(
    request: Request,
    locations : list = Form(...),
    days : int  = Form(...),
    preferences : list = Form(...),
    travel_mode : str = Form(...)
):
    pass

