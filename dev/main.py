from fastapi import FastAPI, Request
from routes.route import app
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from auth.authRouter import auth_router
from planner.planRouter import plan_router
from fastapi.templating import Jinja2Templates

# Initialize FastAPI app
mainApp = FastAPI()

# Set up CORS
mainApp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
mainApp.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
mainApp.include_router(app)
mainApp.include_router(auth_router, prefix="/auth", tags=["auth"])
mainApp.include_router(plan_router)
