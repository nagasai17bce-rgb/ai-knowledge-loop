from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_redaction():
    data=client.post("/v1/run",json={"value":"contact me at user@example.com"}).json()
    assert "[REDACTED]" in data["redacted_ticket"]
    assert data["human_review_required"] is True
