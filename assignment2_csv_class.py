# Assignment 2: Menu driven program - CRUD on CSV file (Employee table) using a class
import csv
import os


class EmployeeCSV:
    def __init__(self, filename="employee.csv"):
        self.filename = filename
        self.fields = ["emp_id", "name", "department", "salary"]

        # if the file is not there yet, create it with the header row
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                csv.writer(f).writerow(self.fields)

    # helper: read every row from the file into a list of dictionaries
    def read_all(self):
        with open(self.filename, "r", newline="") as f:
            return list(csv.DictReader(f))

    # helper: overwrite the file with the given list of rows
    def write_all(self, rows):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)

    # C - create
    def add_employee(self, emp_id, name, department, salary):
        rows = self.read_all()
        for row in rows:
            if row["emp_id"] == emp_id:
                print("Employee ID already exists!")
                return
        rows.append({"emp_id": emp_id, "name": name,
                     "department": department, "salary": salary})
        self.write_all(rows)
        print("Employee added successfully.")

    # R - read
    def view_all(self):
        rows = self.read_all()
        if not rows:
            print("No records found.")
            return
        print("\n{:<8}{:<15}{:<15}{:<10}".format("ID", "Name", "Department", "Salary"))
        print("-" * 48)
        for r in rows:
            print("{:<8}{:<15}{:<15}{:<10}".format(
                r["emp_id"], r["name"], r["department"], r["salary"]))

    def search_employee(self, emp_id):
        for r in self.read_all():
            if r["emp_id"] == emp_id:
                print("Found ->", r["emp_id"], r["name"], r["department"], r["salary"])
                return
        print("Employee not found.")

    # U - update
    def update_employee(self, emp_id, name, department, salary):
        rows = self.read_all()
        found = False
        for r in rows:
            if r["emp_id"] == emp_id:
                r["name"] = name
                r["department"] = department
                r["salary"] = salary
                found = True
        if found:
            self.write_all(rows)
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    # D - delete
    def delete_employee(self, emp_id):
        rows = self.read_all()
        new_rows = [r for r in rows if r["emp_id"] != emp_id]
        if len(new_rows) == len(rows):
            print("Employee not found.")
        else:
            self.write_all(new_rows)
            print("Employee deleted successfully.")


def main():
    emp = EmployeeCSV()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT (CSV) =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp.add_employee(input("ID: "), input("Name: "),
                             input("Department: "), input("Salary: "))
        elif choice == "2":
            emp.view_all()
        elif choice == "3":
            emp.search_employee(input("Enter ID to search: "))
        elif choice == "4":
            emp.update_employee(input("ID to update: "), input("New name: "),
                                input("New department: "), input("New salary: "))
        elif choice == "5":
            emp.delete_employee(input("Enter ID to delete: "))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
