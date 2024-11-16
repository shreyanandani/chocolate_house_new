from app.database import get_db_connection

def manage_flavors():
    print("1. Add Seasonal Flavor")
    print("2. View Seasonal Flavors")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Flavor Name: ")
        description = input("Description: ")
        available_from = input("Available From (YYYY-MM-DD): ")
        available_to = input("Available To (YYYY-MM-DD): ")
        add_seasonal_flavor(name, description, available_from, available_to)
        print("Flavor added successfully!")
    elif choice == "2":
        flavors = get_all_seasonal_flavors()
        for flavor in flavors:
            print(dict(flavor))

def add_seasonal_flavor(name, description, available_from, available_to):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO seasonal_flavors (name, description, available_from, available_to) VALUES (?, ?, ?, ?)",
        (name, description, available_from, available_to),
    )
    conn.commit()
    conn.close()

def get_all_seasonal_flavors():
    conn = get_db_connection()
    flavors = conn.execute("SELECT * FROM seasonal_flavors").fetchall()
    conn.close()
    return flavors
