from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "opportunities.csv"


@dataclass
class RecommendationResult:
    opportunities: list[dict]
    top_skills: list[str]
    missing_skills: list[str]


class OpportunityRecommender:
    def __init__(self, data_path: Path = DATA_PATH) -> None:
        self.data_path = data_path
        self.opportunities = pd.read_csv(data_path)
        self._model = None

    def recommend(self, profile: dict, limit: int = 5) -> RecommendationResult:
        resume_text = self._profile_to_text(profile)
        catalog_text = (
            self.opportunities["title"].fillna("")
            + " "
            + self.opportunities["skills"].fillna("")
            + " "
            + self.opportunities["description"].fillna("")
        ).tolist()

        scores = self._semantic_scores(resume_text, catalog_text)
        ranked = self.opportunities.copy()
        ranked["fit_score"] = np.round(scores * 100, 1)
        ranked = ranked.sort_values("fit_score", ascending=False).head(limit)

        candidate_skills = set(profile.get("skills", []))
        target_skills = self._skills_from_rows(ranked)
        missing = sorted(target_skills - candidate_skills)

        return RecommendationResult(
            opportunities=ranked.to_dict(orient="records"),
            top_skills=sorted(candidate_skills),
            missing_skills=missing[:10],
        )

    def _semantic_scores(self, resume_text: str, catalog_text: list[str]) -> np.ndarray:
        try:
            from sentence_transformers import SentenceTransformer

            if self._model is None:
                self._model = SentenceTransformer("all-MiniLM-L6-v2")
            embeddings = self._model.encode([resume_text, *catalog_text], normalize_embeddings=True)
            return cosine_similarity([embeddings[0]], embeddings[1:])[0]
        except Exception:
            vectorizer = TfidfVectorizer(stop_words="english")
            matrix = vectorizer.fit_transform([resume_text, *catalog_text])
            return cosine_similarity(matrix[0], matrix[1:])[0]

    def _profile_to_text(self, profile: dict) -> str:
        parts = [
            profile.get("summary", ""),
            " ".join(profile.get("skills", [])),
            profile.get("education", ""),
            profile.get("experience", ""),
            profile.get("projects", ""),
        ]
        return " ".join(part for part in parts if part)

    def _skills_from_rows(self, rows: pd.DataFrame) -> set[str]:
        skills: set[str] = set()
        for value in rows["skills"].dropna():
            skills.update(skill.strip().lower() for skill in value.split(",") if skill.strip())
        return skills


def load_opportunities() -> list[dict]:
    return pd.read_csv(DATA_PATH).to_dict(orient="records")
