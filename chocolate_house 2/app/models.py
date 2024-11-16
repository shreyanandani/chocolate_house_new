SCHEMA = """
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    available_from DATE,
    available_to DATE
);

CREATE TABLE IF NOT EXISTS ingredient_inventory (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS customer_feedback (
    id INTEGER PRIMARY KEY,
    name TEXT,
    suggestion TEXT,
    allergy_concern TEXT
);
"""
