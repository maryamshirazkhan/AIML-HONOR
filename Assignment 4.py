# Assignment 4: Menu driven program - CRUD for Employee table using pandas
# (simple functions, no class - data is stored in employee.csv)
import os
import pandas as pd

FILE = "employee.csv"
COLUMNS = ["emp_id", "name", "department", "salary"]


# load the data; if file doesn't exist, start with an empty table
def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame(columns=COLUMNS)


def save_data(df):
    df.to_csv(FILE, index=False)


# C - create
def add_employee():
    df = load_data()
    emp_id = int(input("ID: "))
    if emp_id in df["emp_id"].values:
        print("Employee ID already exists!")
        return
    new_row = {"emp_id": emp_id,
               "name": input("Name: "),
               "department": input("Department: "),
               "salary": float(input("Salary: "))}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    print("Employee added successfully.")


# R - read
def view_all():
    df = load_data()
    if df.empty:
        print("No records found.")
    else:
        print(df.to_string(index=False))


def search_employee():
    df = load_data()
    emp_id = int(input("Enter ID to search: "))
    result = df[df["emp_id"] == emp_id]
    if result.empty:
        print("Employee not found.")
    else:
        print(result.to_string(index=False))


# U - update
def update_employee():
    df = load_data()
    emp_id = int(input("ID to update: "))
    if emp_id not in df["emp_id"].values:
        print("Employee not found.")
        return
    df.loc[df["emp_id"] == emp_id, "name"] = input("New name: ")
    df.loc[df["emp_id"] == emp_id, "department"] = input("New department: ")
    df.loc[df["emp_id"] == emp_id, "salary"] = float(input("New salary: "))
    save_data(df)
    print("Employee updated successfully.")


# D - delete
def delete_employee():
    df = load_data()
    emp_id = int(input("Enter ID to delete: "))
    if emp_id not in df["emp_id"].values:
        print("Employee not found.")
        return
    df = df[df["emp_id"] != emp_id]
    save_data(df)
    print("Employee deleted successfully.")


def main():
    while True:
        print("\n===== EMPLOYEE MANAGEMENT (PANDAS) =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
