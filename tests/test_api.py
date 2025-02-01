import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_faq():
    response = client.post(
        "/faqs/",
        json={
            "question_en": "What is Django?",
            "answer_en": "Django is a high-level Python web framework."
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["question_en"] == "What is Django?"
    assert "translations" in data

def test_get_faqs():
    # Create a test FAQ first
    client.post(
        "/faqs/",
        json={
            "question_en": "Test Question",
            "answer_en": "Test Answer"
        }
    )
    
    response = client.get("/faqs/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    
    # Test with language parameter
    response = client.get("/faqs/?lang=hi")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(t["language"] == "hi" for faq in data for t in faq["translations"])