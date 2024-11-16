from app.handlers import seasonal_flavors, inventory, customer_feedback
from app.database import setup_database

def main():
    print("Welcome to the Chocolate House!")
    print("1. Manage Seasonal Flavors")
    print("2. Manage the Inventory")
    print("3. Customer Feedback")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Dictionary simulating a switch-case structure
    options = {
        "1": seasonal_flavors.manage_flavors,
        "2": inventory.manage_inventory,
        "3": customer_feedback.handle_feedback,
        "4": lambda: print("Goodbye, Thanks!")
    }

    # Get the function from the dictionary and call it, or print an error
    action = options.get(choice)
    
    if action:
        action()  # Call the selected function
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    setup_database()
    main()
