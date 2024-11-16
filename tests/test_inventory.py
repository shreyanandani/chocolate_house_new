import pytest
import sqlite3
from app.handlers.inventory import add_ingredient, update_quantity, get_inventory
from app.database import get_db_connection

@pytest.fixture
def test_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
    CREATE TABLE ingredient_inventory (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit TEXT NOT NULL
    );
    """)
    yield conn
    conn.close()

def test_add_ingredient(test_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    add_ingredient("Cocoa Powder", 10, "kg")
    inventory = get_inventory()

    assert len(inventory) == 1
    assert inventory[0]["name"] == "Cocoa Powder"
    assert inventory[0]["quantity"] == 10

def test_update_quantity(test_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    add_ingredient("Milk Powder", 5, "kg")
    update_quantity("Milk Powder", 10)
    inventory = get_inventory()

    assert inventory[0]["quantity"] == 15

def test_insufficient_inventory(test_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db_connection", lambda: test_db)

    add_ingredient("Sugar", 0, "kg")
    inventory = get_inventory()

    assert inventory[0]["quantity"] == 0
