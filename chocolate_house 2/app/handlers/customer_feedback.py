from app.database import get_db_connection

def handle_feedback():
    print("1. Add Customer Feedback")
    print("2. View Feedback")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Customer Name: ")
        suggestion = input("Flavor Suggestion: ")
        allergy_concern = input("Allergy Concern (if any): ")
        add_feedback(name, suggestion, allergy_concern)
        print("Feedback submitted successfully!")
    elif choice == "2":
        feedback = get_feedback()
        for fb in feedback:
            print(dict(fb))

def add_feedback(name, suggestion, allergy_concern):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO customer_feedback (name, suggestion, allergy_concern) VALUES (?, ?, ?)",
        (name, suggestion, allergy_concern),
    )
    conn.commit()
    conn.close()

def get_feedback():
    conn = get_db_connection()
    feedback = conn.execute("SELECT * FROM customer_feedback").fetchall()
    conn.close()
    return feedback
