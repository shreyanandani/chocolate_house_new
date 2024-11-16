# Chocolate House Management Application

This Python application manages a fictional chocolate house using SQLite. It handles:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

---

## **Features**
- **Manage Seasonal Flavors**: Add, update, and remove seasonal chocolate flavors.
- **Ingredient Inventory**: Track ingredients and their quantities.
- **Customer Feedback**: Collect customer flavor suggestions and allergy concerns.

---

## **Tech Stack**
- **Python** (3.x)
- **SQLite** (for database storage)
- **Docker** (for containerization)

---

## **Setup and Installation**

### **1. Clone the Repository**

Clone the project to your local machine:


git clone https://github.com/yourusername/chocolate_house.git
cd chocolate_house
### **2. Create and Activate Virtual Environment**

It's recommended to use a virtual environment for this project to avoid dependency conflicts.

#### **For macOS/Linux**:


python3 -m venv venv
source venv/bin/activate
#### **For Windows**:


python -m venv venv
venv\Scripts\activate
### **3. Install Dependencies**

Install the required dependencies using `pip`:


pip install -r requirements.txt
### **4. Database Setup**

The SQLite database schema will be created automatically when you run the application. If you want to manually initialize the database schema, run the following command:


PYTHONPATH=. python3 app/main.py
### **5. Running the Application**

To start the application, simply run:


PYTHONPATH=. python3 app/main.py
### **6. Testing the Application**

The application has a basic testing suite. To run the tests, execute the following command:


pytest
#### **Test Steps**

- **Test for Seasonal Flavors**: Verify that flavors can be added, fetched, and removed from the database.
- **Test for Inventory**: Ensure that ingredients can be tracked by name, quantity, and unit.
- **Test for Customer Feedback**: Check if customer suggestions and allergy concerns are properly stored and retrieved.
### **7. Dockerized Build and Run**

The project can also be run in a Docker container for consistency across different environments.

#### **1. Build the Docker Image**

From the project root directory, run the following command to build the Docker image:


docker build -t chocolate-house .
#### **2. Run the Application in Docker**

Once the image is built, run the application using the following command:


docker run -p 5000:5000 chocolate-house
### **File Structure
chocolate_house/
├── app/
│   ├── database.py           # Handles database connection and schema setup
│   ├── main.py               # Entry point to the application
│   ├── handlers/             # Business logic for flavors, inventory, and feedback
│   │   ├── seasonal_flavors.py
│   │   ├── inventory.py
│   │   └── customer_feedback.py
│   ├── schema.sql            # SQL schema to set up the database
├── tests/                    # Contains test cases for the application
│   ├── test_seasonal_flavors.py
│   ├── test_inventory.py
│   └── test_customer_feedback.py
├── Dockerfile                # Dockerfile to build the Docker image
├── requirements.txt          # Project dependencies
└── README.md                 # This file
### **9. Code Documentation**

- **`database.py`**:  
  Contains functions for connecting to the SQLite database, setting up tables from `schema.sql`, and performing database operations.

- **`handlers/`**:  
  Contains the core logic for managing:
  - **Seasonal Flavors** (`seasonal_flavors.py`)
  - **Inventory** (`inventory.py`)
  - **Customer Feedback** (`customer_feedback.py`)

- **`schema.sql`**:  
  SQL file to set up the database schema.

- **Tests**:  
  Ensure that the application works as expected, with separate test files for:
  - Seasonal Flavors
  - Inventory
  - Customer Feedback
### **10. Edge Scenarios Handled**

- **Missing `schema.sql` File**:  
  If the `schema.sql` file is missing, the application will raise a `FileNotFoundError` and notify the user.

- **Duplicate Entries**:  
  Ensures that duplicate entries for seasonal flavors and inventory items are not allowed.

- **Invalid Input**:  
  Handles invalid inputs when interacting with the database, such as:
  - Negative quantities
  - Incorrect date formats
  - Missing required fields
### **11. Contributing**

We welcome contributions to improve this project! Follow the steps below to contribute:

1. **Fork the Repository**:  
   Click the "Fork" button at the top right corner of the repository page to create your copy of the repository.

2. **Clone Your Fork**:  
   Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/your-username/chocolate_house.git
   cd chocolate_house
### **12. License**

This project is licensed under the MIT License.  

You are free to use, modify, and distribute this software as long as the original license is included in any distributions or derivative works.  

For more details, see the [LICENSE](LICENSE) file included in this repository.
