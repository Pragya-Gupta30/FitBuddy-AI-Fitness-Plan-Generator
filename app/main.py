from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.ai_generator import generate_workout_plan, update_workout_plan, generate_nutrition_tip
from app.database import engine, get_db
from app.models import Base
from app.crud import save_user, save_workout_plan, update_workout_plan_db, get_all_users_with_plans

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    username: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db)
):
    # Generate workout plan and nutrition tip
    workout_plan = generate_workout_plan(age, weight, goal, intensity)
    nutrition_tip = generate_nutrition_tip(goal)
    
    # Save user data to database
    user = save_user(db, username, age, weight, goal, intensity)
    
    # Save workout plan to database
    workout_plan_record = save_workout_plan(db, user.id, workout_plan)
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": username,
        "age": age,
        "weight": weight,
        "goal": goal,
        "intensity": intensity,
        "workout_plan": workout_plan,
        "nutrition_tip": nutrition_tip,
        "show_user_info": True,
        "workout_plan_id": workout_plan_record.id
    })

@app.post("/submit-feedback", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    original_plan: str = Form(...),
    feedback: str = Form(...),
    workout_plan_id: int = Form(None),
    db: Session = Depends(get_db)
):
    # Generate updated plan
    updated_plan = update_workout_plan(original_plan, feedback)
    
    # Update workout plan in database if workout_plan_id is provided
    if workout_plan_id:
        update_workout_plan_db(db, workout_plan_id, updated_plan)
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "workout_plan": updated_plan,
        "show_user_info": False,
        "workout_plan_id": workout_plan_id
    })

@app.get("/view-all-users", response_class=HTMLResponse)
async def view_all_users(request: Request, db: Session = Depends(get_db)):
    """
    Admin page to view all users and their workout plans.
    """
    users = get_all_users_with_plans(db)
    return templates.TemplateResponse("all_users.html", {
        "request": request,
        "users": users
    })
