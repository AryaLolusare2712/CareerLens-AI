# AI Career Opportunity Matcher

A Python + Streamlit + FastAPI starter project for resume analysis, skill-gap insights, opportunity recommendations, recruiter review, and analytics.

## What Is Included

- Streamlit dashboard with resume upload, recommendations, recruiter portal, and analytics
- FastAPI backend with resume analysis and recommendation endpoints
- Resume parsing for PDF, DOCX, and TXT files
- Hybrid recommendation engine using sentence-transformers when available and TF-IDF fallback
- Gemini integration hook for AI summary/career guidance when `GEMINI_API_KEY` is set
- Sample internship, hackathon, scholarship, and job data

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the backend:

```powershell
uvicorn backend.main:app --reload --port 8000
```

Start the frontend in another terminal:

```powershell
streamlit run streamlit_app.py
```

The app also works in demo mode if the backend is not running.

## Optional Gemini Setup

Create a `.env` file from `.env.example` and set:

```text
GEMINI_API_KEY=your_key_here
```

## Project Structure

```text
backend/
  main.py              FastAPI app and API routes
  recommender.py       Matching, ranking, and skill-gap logic
  resume_parser.py     PDF/DOCX/TXT extraction helpers
data/
  opportunities.csv    Demo opportunity catalog
streamlit_app.py       Streamlit frontend
requirements.txt       Python dependencies
```
