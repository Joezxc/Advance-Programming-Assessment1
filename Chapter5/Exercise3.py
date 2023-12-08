import tkinter as tk

class Employee:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.id = ""
        self.salary = ""

    def setData(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.id = emp_id
        self.salary = salary

    def getData(self):
        return f"{self.name}\t{self.age}\t{self.salary}\t{self.id}"

employees = []

def add_employee():
    # Retrieve data from Entry fields
    name = name_entry.get()
    age = age_entry.get()
    emp_id = id_entry.get()
    salary = salary_entry.get()

    # Create a new Employee object
    emp = Employee()

    # Set the data of the Employee object using the data retrieved from Entry fields
    emp.setData(name, age, emp_id, salary)

    # Add the Employee object to the list of employees
    employees.append(emp)

def display_employees():
    # Clear the result Text widget
    result_text.delete(1.0, tk.END)

    # Loop through the list of employees and insert their data into the result Text widget
    for emp in employees:
        result_text.insert(tk.END, emp.getData() + "\n")

root = tk.Tk()
root.title("Employee Management")

# Create Labels and Entry fields for the user to input employee data
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="ID").grid(row=2, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Salary").grid(row=3, column=0, padx=10, pady=5)
salary_entry = tk.Entry(root)
salary_entry.grid(row=3, column=1, padx=10, pady=5)

# Create a Button for adding an employee and set its command to the add_employee function
add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a Button for displaying all employees and set its command to the display_employees function
display_button = tk.Button(root, text="Display Employees", command=display_employees)
display_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create a Text widget to display the results
result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()