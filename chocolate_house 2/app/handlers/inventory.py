from app.database import get_db_connection

def manage_inventory():
    print("1. Add Ingredient")
    print("2. Update Ingredient Quantity")
    print("3. View Inventory")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Ingredient Name: ")
        quantity = int(input("Quantity: "))
        unit = input("Unit (e.g., kg, g, ml): ")
        add_ingredient(name, quantity, unit)
        print("Ingredient added successfully!")
    elif choice == "2":
        name = input("Ingredient Name: ")
        quantity = int(input("Quantity to Add: "))
        update_quantity(name, quantity)
        print("Quantity updated successfully!")
    elif choice == "3":
        inventory = get_inventory()
        for item in inventory:
            print(dict(item))

def add_ingredient(name, quantity, unit):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO ingredient_inventory (name, quantity, unit) VALUES (?, ?, ?)",
        (name, quantity, unit),
    )
    conn.commit()
    conn.close()

def update_quantity(name, quantity):
    conn = get_db_connection()
    conn.execute(
        "UPDATE ingredient_inventory SET quantity = quantity + ? WHERE name = ?",
        (quantity, name),
    )
    conn.commit()
    conn.close()

def get_inventory():
    conn = get_db_connection()
    inventory = conn.execute("SELECT * FROM ingredient_inventory").fetchall()
    conn.close()
    return inventory
