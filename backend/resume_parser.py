from __future__ import annotations

import re
from pathlib import Path
from typing import BinaryIO


COMMON_SKILLS = {
    "python",
    "java",
    "c++",
    "sql",
    "postgresql",
    "mongodb",
    "fastapi",
    "streamlit",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "nlp",
    "transformers",
    "bert",
    "sentence-transformers",
    "faiss",
    "scikit-learn",
    "pandas",
    "numpy",
    "plotly",
    "matplotlib",
    "spacy",
    "nltk",
    "pymupdf",
    "pdfplumber",
    "python-docx",
    "jwt",
    "oauth",
    "redis",
    "websockets",
    "langchain",
    "crewai",
    "beautifulsoup",
    "selenium",
    "requests",
    "data visualization",
    "statistics",
    "analytics",
    "communication",
    "teamwork",
    "ui design",
}


def extract_text_from_upload(file: BinaryIO, filename: str) -> str:
    suffix = Path(filename).suffix.lower()
    data = file.read()

    if suffix == ".pdf":
        return _extract_pdf_text(data)
    if suffix == ".docx":
        return _extract_docx_text(data)
    return data.decode("utf-8", errors="ignore")


def extract_profile(text: str) -> dict:
    cleaned = normalize_text(text)
    skills = extract_skills(cleaned)
    return {
        "summary": summarize_text(cleaned),
        "skills": skills,
        "education": extract_section(cleaned, ["education", "qualification"]),
        "experience": extract_section(cleaned, ["experience", "work history", "internship"]),
        "projects": extract_section(cleaned, ["projects", "project work"]),
        "word_count": len(cleaned.split()),
    }


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def summarize_text(text: str, max_words: int = 70) -> str:
    words = text.split()
    if not words:
        return "No resume text could be extracted."
    return " ".join(words[:max_words]) + ("..." if len(words) > max_words else "")


def extract_skills(text: str) -> list[str]:
    lower = text.lower()
    found = [skill for skill in COMMON_SKILLS if re.search(rf"(?<!\w){re.escape(skill)}(?!\w)", lower)]
    return sorted(found)


def extract_section(text: str, headings: list[str], max_chars: int = 420) -> str:
    lower = text.lower()
    for heading in headings:
        idx = lower.find(heading)
        if idx >= 0:
            return text[idx : idx + max_chars].strip()
    return ""


def _extract_pdf_text(data: bytes) -> str:
    import fitz

    doc = fitz.open(stream=data, filetype="pdf")
    return "\n".join(page.get_text() for page in doc)


def _extract_docx_text(data: bytes) -> str:
    from docx import Document
    from io import BytesIO

    document = Document(BytesIO(data))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)
