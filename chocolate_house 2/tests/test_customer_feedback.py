import pytest
import sqlite3
from app.handlers.customer_feedback import add_feedback, get_feedback
from app.database import get_db_connection

@pytest.fixture
def test_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
    CREATE TABLE customer_feedback (
        id INTEGER PRIMARY KEY,
        name TEXT,
        suggestion TEXT,
        allergy_concern TEXT
    );
    """)
    yield conn
    conn.close()

def test_add_feedback(test_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    add_feedback("John Doe", "Mint Chocolate", "Lactose Intolerance")
    feedback = get_feedback()

    assert len(feedback) == 1
    assert feedback[0]["name"] == "John Doe"

def test_multiple_feedbacks(test_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    add_feedback("Alice", "Dark Chocolate", "Nut Allergy")
    add_feedback("Bob", "White Chocolate", None)
    feedback = get_feedback()

    assert len(feedback) == 2
    assert feedback[1]["name"] == "Bob"
    assert feedback[1]["allergy_concern"] is None
