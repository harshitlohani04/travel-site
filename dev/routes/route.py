from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.model import User


app = APIRouter()

template = Jinja2Templates(directory="templates")

# CORS : Cross-Origin Resource Sharing
# prefferably used in cases when the fromtend is running on a different host and the backend on a different.
# The requests are then blocked by the browser due to security concerns.

@app.get("/", response_class=HTMLResponse)
async def display_function(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "result": None})

