from models.db import supabase_client
from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Form

auth_router = APIRouter()

template_auth = Jinja2Templates(directory="templates")

print("Auth code loaded")

@auth_router.get("/signup", response_class=HTMLResponse)
async def get_signup_page(request: Request):
    return template_auth.TemplateResponse("auth.html", {"request": request})

@auth_router.post("/signup", response_class=HTMLResponse)
async def auth_page_signup(
                    request: Request,
                    username: str = Form(...),
                    email: str = Form(...),
                    password: str = Form(...)):
    try:
        existing_user = (
            supabase_client.table("users")
            .select("*")
            .eq("email", email)
            .execute()
        )
        if existing_user.data:
            raise HTTPException(status_code=400, detail="User already exists")
        response = (
            supabase_client.table("users").insert({
                "username": username,
                "email": email,
                "password": password
            }).execute()
        )
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        return template_auth.TemplateResponse(
            "auth.html",
            {"request": request, "error": str(e)}
        )

@auth_router.post("/signin", response_class=HTMLResponse)
async def auth_page_signin(
                    request: Request,
                    username: str = Form(...),
                    password: str = Form(...)):
    try:
        user = (
            supabase_client.table("users")
            .select("*")
            .eq("username", username)
            .eq("password", password)
            .execute()
        )
        if not user.data:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        return template_auth.TemplateResponse(
            "auth.html",
            {"request": request, "error": str(e)}
        )
