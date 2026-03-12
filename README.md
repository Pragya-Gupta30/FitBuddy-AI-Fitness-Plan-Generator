# FitBuddy-AI-Fitness-Plan-Generator
FitBuddy – AI Fitness Plan Generator
FitBuddy is an AI-powered web application that generates personalized 7-day workout plans and nutrition tips based on a user’s fitness profile. The system collects user details such as age, weight, fitness goal, and workout intensity, then uses Generative AI to create structured and goal-oriented fitness routines.

The application also allows users to submit feedback to update their workout plans, ensuring the plan adapts to their evolving fitness needs. All user information and workout plans are stored in a SQLite database and can be viewed through an admin dashboard.

Features
AI generated 7-day workout plans

Personalized nutrition & recovery tips

User feedback system to update workout plans

Admin dashboard to view all users and their plans

SQLite database for storing user data

Clean and responsive UI using HTML templates

Built with FastAPI backend

Tech Stack
Backend

FastAPI

Python

Database

SQLite

SQLAlchemy

Frontend

HTML

Jinja2 Templates

CSS

AI Integration

Generative AI API (Gemini-style workout generation)

Project Structure

fitbuddy
│
├── app
│   ├── main.py
│   ├── ai_generator.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   └── templates
│       ├── index.html
│       ├── result.html
│       └── all_users.html
│
├── fitbuddy.db
├── requirements.txt
├── README.md
└── .env
How to Run the Project
1. Clone the repository

git clone https://github.com/YOUR_USERNAME/fitbuddy.git
cd fitbuddy
2. Install dependencies

pip install -r requirements.txt
3. Add your API key
Create a .env file and add:


GROQ_API_KEY=your_api_key_here
4. Run the FastAPI server

uvicorn app.main:app --reload
5. Open the application
Open your browser and go to:


http://127.0.0.1:8000
FastAPI API docs are available at:


http://127.0.0.1:8000/docs
Application Pages
Home Page
Users enter their:

Name

User ID

Age

Weight

Fitness Goal

Workout Intensity

After submission, the AI generates a personalized workout plan.

Personalized Workout Page
Displays:

User profile

Generated 7-day workout plan

Nutrition & recovery tip

Option to update plan using feedback

Feedback Feature
Users can submit feedback like:

"Add more cardio"

"Make workouts easier"

The AI updates the workout plan accordingly.

Admin Dashboard
The View All Users page displays:

User details

Original workout plan

Updated workout plan

This helps monitor user plans and feedback updates.

Example Use Cases
Scenario 1
A user enters their fitness details and receives a personalized 7-day workout plan tailored to their goals and workout intensity.

Scenario 2
The user provides feedback on the generated workout plan, and the system regenerates an updated plan.

Scenario 3
The system provides a nutrition or recovery tip aligned with the user’s fitness goal.

Future Improvements
Authentication system for users

BMI and calorie calculation

Exercise video recommendations

Deployment on cloud platforms
