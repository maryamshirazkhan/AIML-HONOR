# Assignment 3: Menu driven program - CRUD on Database (Employee table) using a class
# Uses sqlite3 - it comes built into Python, so nothing to install
import sqlite3


class EmployeeDB:
    def __init__(self, db_name="company.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        # create the table the first time the program runs
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                emp_id     INTEGER PRIMARY KEY,
                name       TEXT NOT NULL,
                department TEXT,
                salary     REAL
            )
        """)
        self.conn.commit()

    # C - create
    def add_employee(self, emp_id, name, department, salary):
        try:
            self.cur.execute("INSERT INTO employee VALUES (?, ?, ?, ?)",
                             (emp_id, name, department, salary))
            self.conn.commit()
            print("Employee added successfully.")
        except sqlite3.IntegrityError:
            print("Employee ID already exists!")

    # R - read
    def view_all(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()
        if not rows:
            print("No records found.")
            return
        print("\n{:<8}{:<15}{:<15}{:<10}".format("ID", "Name", "Department", "Salary"))
        print("-" * 48)
        for r in rows:
            print("{:<8}{:<15}{:<15}{:<10}".format(r[0], r[1], r[2], r[3]))

    def search_employee(self, emp_id):
        self.cur.execute("SELECT * FROM employee WHERE emp_id = ?", (emp_id,))
        row = self.cur.fetchone()
        if row:
            print("Found ->", row)
        else:
            print("Employee not found.")

    # U - update
    def update_employee(self, emp_id, name, department, salary):
        self.cur.execute(
            "UPDATE employee SET name=?, department=?, salary=? WHERE emp_id=?",
            (name, department, salary, emp_id))
        self.conn.commit()
        if self.cur.rowcount == 0:
            print("Employee not found.")
        else:
            print("Employee updated successfully.")

    # D - delete
    def delete_employee(self, emp_id):
        self.cur.execute("DELETE FROM employee WHERE emp_id = ?", (emp_id,))
        self.conn.commit()
        if self.cur.rowcount == 0:
            print("Employee not found.")
        else:
            print("Employee deleted successfully.")

    def close(self):
        self.conn.close()


def main():
    emp = EmployeeDB()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT (DATABASE) =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp.add_employee(int(input("ID: ")), input("Name: "),
                             input("Department: "), float(input("Salary: ")))
        elif choice == "2":
            emp.view_all()
        elif choice == "3":
            emp.search_employee(int(input("Enter ID to search: ")))
        elif choice == "4":
            emp.update_employee(int(input("ID to update: ")), input("New name: "),
                                input("New department: "), float(input("New salary: ")))
        elif choice == "5":
            emp.delete_employee(int(input("Enter ID to delete: ")))
        elif choice == "6":
            emp.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
