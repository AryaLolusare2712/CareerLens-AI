from __future__ import annotations

import os
from functools import lru_cache

from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .recommender import OpportunityRecommender, load_opportunities
from .resume_parser import extract_profile, extract_text_from_upload


load_dotenv()

app = FastAPI(title="AI Career Opportunity Matcher API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProfilePayload(BaseModel):
    summary: str = ""
    skills: list[str] = []
    education: str = ""
    experience: str = ""
    projects: str = ""


@lru_cache
def get_recommender() -> OpportunityRecommender:
    return OpportunityRecommender()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/opportunities")
def opportunities() -> list[dict]:
    return load_opportunities()


@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)) -> dict:
    text = extract_text_from_upload(file.file, file.filename or "resume.txt")
    profile = extract_profile(text)
    profile["ai_guidance"] = generate_guidance(profile)
    return profile


@app.post("/recommend")
def recommend(profile: ProfilePayload, limit: int = 5) -> dict:
    result = get_recommender().recommend(profile.model_dump(), limit=limit)
    return {
        "opportunities": result.opportunities,
        "top_skills": result.top_skills,
        "missing_skills": result.missing_skills,
    }


@app.get("/recruiter/candidates")
def recruiter_candidates() -> list[dict]:
    return [
        {"name": "Aarav Sharma", "role": "ML Intern", "fit_score": 91, "skills": ["python", "nlp", "pandas"]},
        {"name": "Mira Iyer", "role": "Streamlit Developer", "fit_score": 86, "skills": ["streamlit", "plotly", "sql"]},
        {"name": "Kabir Khan", "role": "Backend API Intern", "fit_score": 82, "skills": ["fastapi", "postgresql", "jwt"]},
    ]


def generate_guidance(profile: dict) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        skills = ", ".join(profile.get("skills", [])[:8]) or "your strongest technical skills"
        return f"Demo guidance: highlight {skills}, add measurable project outcomes, and tailor your resume to the top missing skills."

    try:
        import google.generativeai as genai

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            "Give concise career guidance for this student profile. Include strengths, missing skills, "
            f"and next steps:\n{profile}"
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as exc:
        return f"Gemini guidance unavailable: {exc}"
