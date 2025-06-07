from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from ML.planner import get_planner

plan_router = APIRouter()

templates = Jinja2Templates(directory="templates")

@plan_router.get("/planner", response_class=HTMLResponse)
async def get_planner_page(request: Request):
    return templates.TemplateResponse("planner.html", {"request": request})

@plan_router.post("/planner", response_class=HTMLResponse)
async def plan_page(
    request: Request,
    locations : str = Form(...),
    days : int  = Form(...),
    preferences : str = Form(...),
    travelmode : str = Form(...)
):
    locations_arr = locations.replace(" ", "").split(",")
    preferences_arr = preferences.replace(" ", "").split(",")

    userTravelData = {
        "locations": locations_arr,
        "days": days,
        "preferences": preferences_arr,
        "travel_mode": travelmode
    }

    try:
        plannerResponse = get_planner(userTravelData)
        return templates.TemplateResponse("plan.html", {"request": request, "result": plannerResponse})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating plan: {str(e)}")
