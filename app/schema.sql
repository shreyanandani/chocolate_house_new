-- Create table for seasonal flavors
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    available_from DATE NOT NULL,
    available_to DATE NOT NULL
);

-- Create table for ingredient inventory
CREATE TABLE IF NOT EXISTS ingredient_inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit TEXT NOT NULL
);

-- Create table for customer feedback
CREATE TABLE IF NOT EXISTS customer_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    suggestion TEXT NOT NULL,
    allergy_concern TEXT
);