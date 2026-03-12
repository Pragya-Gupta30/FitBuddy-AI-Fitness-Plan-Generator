from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("API_KEY"))
def generate_workout_plan(age, weight, goal, intensity):

    prompt = f"""
Create a structured 7-day workout plan.

Age: {age}
Weight: {weight}
Goal: {goal}
Workout Intensity: {intensity}

Include:
- warmup
- main exercises with sets and reps
- cooldown
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def update_workout_plan(original_plan: str, feedback: str) -> str:
    """
    Update the workout plan based on user feedback using Groq's Llama3 model.
    """
    prompt = f"""
You are a fitness expert. A user has received the following workout plan:

{original_plan}

The user has provided this feedback:
{feedback}

Please update the workout plan based on their feedback. Keep the same structure (7-day plan with warmup, main exercises, and cooldown) but modify it according to their requests. Make sure the updated plan is realistic and safe.
"""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error updating workout plan: {str(e)}"

def generate_nutrition_tip(goal: str) -> str:
    """
    Generate a short nutrition or recovery tip based on the user's fitness goal.
    """
    prompt = f"""
You are a nutrition and fitness expert. Generate a concise, practical nutrition or recovery tip for someone whose fitness goal is: {goal}

The tip should be:
- Short and actionable (2-4 sentences)
- Specific to their fitness goal
- Easy to implement
- Evidence-based

Focus on either nutrition advice or recovery strategies that will help them achieve their goal.
"""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating nutrition tip: {str(e)}"