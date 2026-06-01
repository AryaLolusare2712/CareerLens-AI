#  CareerLens AI  
### AI Opportunity Recommendation & Talent Matchmaking Platform

> Helping students discover better opportunities and enabling smarter recruiter matchmaking through AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![AI](https://img.shields.io/badge/AI-Gemini%20%7C%20NLP-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

---

#  Problem Statement

Students often struggle to find opportunities that genuinely match their skills, interests, and eligibility.

Most existing platforms focus mainly on listings and broad discovery, leaving students uncertain about:

- What opportunities they are eligible for
- Which skills they are missing
- Which internships or hackathons fit them best
- How to improve their selection chances

At the same time, recruiters and startups face challenges such as:

- Large applicant pools
- Manual screening
- Resume overload
- Weak candidate-job matching

**CareerLens AI** aims to solve both sides of this problem through AI-powered recommendation and talent matchmaking.

---

#  What is CareerLens AI?

**CareerLens AI** is an AI-powered platform designed for both:

###  Students
Discover personalized opportunities and understand career readiness.

###  Recruiters
Identify and screen better-fit student talent faster.

Instead of functioning as just another listing platform, CareerLens AI acts as a **career intelligence and matchmaking system**.

---

#  Core Features

##  AI Resume Intelligence

Upload:

- PDF
- DOCX
- TXT

AI extracts:

- Skills
- Education
- Projects
- Experience
- Profile summary

---

##  Opportunity Recommendation Engine

Recommend:

- Internships
- Jobs
- Hackathons
- Scholarships
- Open-source programs

using:

- Semantic similarity
- NLP embeddings
- Hybrid recommendation logic

---

##  Skill Gap Detection

CareerLens AI identifies:

> Skills preventing stronger opportunity matches

Example:

```text
Current Match: 72%
Learn Docker + FastAPI → Match could improve to 88%
```

---

##  Recruiter Matchmaking

Recruiters can:

- Discover talent faster
- Reduce screening effort
- Filter intelligently
- View AI-generated fit scores

Possible filters:

- Graduation year
- Skill stack
- Internship duration
- Availability
- College tier
- Domain

---

#  Tech Stack

## Frontend
- Streamlit
- Plotly

## Backend
- FastAPI
- Python

## AI / NLP
- Gemini API
- Sentence Transformers
- spaCy
- Scikit-learn

## Recommendation Engine
- FAISS
- Cosine Similarity
- TF-IDF fallback

## Resume Parsing
- PyMuPDF
- python-docx
- pdfplumber

## Database
- PostgreSQL

---

#  System Architecture

```text
Resume Upload
      ↓
Resume Parsing
      ↓
Skill Extraction
      ↓
Embedding Generation
      ↓
Opportunity Database
      ↓
AI Matching Engine
      ↓
Fit Score + Recommendations
      ↓
Recruiter Screening + Analytics
```

---

#  Project Structure

```text
backend/
│
├── main.py
├── recommender.py
├── resume_parser.py
│
data/
├── opportunities.csv
│
streamlit_app.py
requirements.txt
README.md
```

---

#  Installation

## 1. Clone Repository

```bash
git clone https://github.com/AryaLolusare2712/CareerLens-AI
cd CareerLens-AI
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Running CareerLens AI

## Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

## Frontend

```bash
streamlit run streamlit_app.py
```

The platform also supports **demo mode** if the backend is unavailable.

---

#  Gemini Setup (Optional)

Create:

```text
.env
```

Add:

```text
GEMINI_API_KEY=your_api_key
```

Used for:

- AI summaries
- Career guidance
- Personalized recommendations

---

#  Future Roadmap

- Live opportunity scraping
- LinkedIn/GitHub integration
- Recruiter dashboard
- Resume builder
- AI screening workflows
- Interview preparation
- Multi-agent recommendation system

---

#  Vision

CareerLens AI aims to become:

> A career intelligence and AI-powered talent matchmaking ecosystem for students and recruiters.

---

#  Author

**Arya Lolusare**

AI • LLM • Recommendation Systems • Full-Stack Development

GitHub:
https://github.com/AryaLolusare2712
