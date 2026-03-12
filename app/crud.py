from sqlalchemy.orm import Session
from app.models import User, WorkoutPlan

def save_user(db: Session, name: str, age: int, weight: float, goal: str, intensity: str):
    """
    Save user data to the database.
    """
    user = User(
        name=name,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def save_workout_plan(db: Session, user_id: int, original_plan: str):
    """
    Save generated workout plan to the database.
    """
    workout_plan = WorkoutPlan(
        user_id=user_id,
        original_plan=original_plan
    )
    db.add(workout_plan)
    db.commit()
    db.refresh(workout_plan)
    return workout_plan

def update_workout_plan_db(db: Session, workout_plan_id: int, updated_plan: str):
    """
    Update workout plan after feedback.
    """
    workout_plan = db.query(WorkoutPlan).filter(WorkoutPlan.id == workout_plan_id).first()
    if workout_plan:
        workout_plan.updated_plan = updated_plan
        db.commit()
        db.refresh(workout_plan)
    return workout_plan

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieve user by ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_workout_plan_by_id(db: Session, workout_plan_id: int):
    """
    Retrieve workout plan by ID.
    """
    return db.query(WorkoutPlan).filter(WorkoutPlan.id == workout_plan_id).first()

def get_user_workout_plans(db: Session, user_id: int):
    """
    Get all workout plans for a specific user.
    """
    return db.query(WorkoutPlan).filter(WorkoutPlan.user_id == user_id).all()

def get_all_users_with_plans(db: Session):
    """
    Get all users with their workout plans.
    """
    return db.query(User).all()
