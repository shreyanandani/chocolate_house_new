import pytest
import sqlite3
from app.handlers.seasonal_flavors import add_seasonal_flavor, get_all_seasonal_flavors
from app.database import get_db_connection

@pytest.fixture
def test_db():
    # Create a temporary database
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
    CREATE TABLE seasonal_flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        available_from DATE,
        available_to DATE
    );
    """)
    yield conn
    conn.close()

def test_add_seasonal_flavor(test_db, monkeypatch):
    # Override the connection to use the test database
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    add_seasonal_flavor("Pumpkin Spice", "Fall special", "2024-10-01", "2024-11-30")
    flavors = get_all_seasonal_flavors()

    assert len(flavors) == 1
    assert flavors[0]["name"] == "Pumpkin Spice"

def test_invalid_date(test_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    with pytest.raises(Exception):
        add_seasonal_flavor("Summer Delight", "Hot season special", "invalid-date", "2024-09-01")
