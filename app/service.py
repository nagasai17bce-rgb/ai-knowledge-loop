import re

class Service:
    def run(self, value: str):
        clean = re.sub(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", "[REDACTED]", value)
        return {
            "redacted_ticket": clean,
            "novelty_check": "pending",
            "draft_title": "Support resolution candidate",
            "human_review_required": True,
        }
