# AI Knowledge Loop

A safe starting point for turning support interactions into reusable knowledge. The demo redacts email addresses and emits a review-required knowledge candidate.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Production extensions
Add duplicate/novelty detection, resolution extraction, source provenance, reviewer workflows, publishing gates, and feedback-driven ranking.
