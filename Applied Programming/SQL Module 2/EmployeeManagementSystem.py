import sqlite3
from EmployeeClass import Employee

connection = sqlite3.connect('employee.db')

cursor = connection.cursor()



# cursor.execute("""
# CREATE TABLE departments(
#     DepartmentID INTEGER,
#     DepartmentName TEXT
# )""")

# cursor.execute("INSERT INTO departments VALUES('1', 'Technology')")
# cursor.execute("INSERT INTO departments VALUES('2', 'Medical')")
# cursor.execute("INSERT INTO departments VALUES('3', 'Educational')")
# connection.commit()


# cursor.execute("""
# CREATE TABLE employees (
#     EmployeeID INTEGER,
#     FirstName TEXT,
#     LastName TEXT,
#     Position TEXT,
#     Salary REAL,
#     HireDate TEXT,
#     DepartmentID INTEGER           
# )""")
# connection.commit()



# cursor.execute("INSERT INTO employees VALUES ('1','Noah','Carrier','Software Developer','60000','5/11/2024')")

# cursor.execute("INSERT INTO employees VALUES ('2','Sarah','Carrier','Assisted Living Aid','90000','5/15/2024')")

#emp_1 = Employee(3,'John','Doe','Janiter',20000,'1/2/1987')
#emp_2 = Employee(4,'Jane','Doe','Teacher', 20000, '1/8/1999')

# cursor.execute("INSERT INTO employees VALUES (?,?,?,?,?,?)",(emp_1.id,emp_1.firstname,emp_1.lastname,emp_1.position,emp_1.salary,emp_1.hireDate))

# connection.commit()

# cursor.execute("INSERT INTO employees VALUES (:id,:first,:last,:position,:pay,:hired)",{'id':emp_2.id,'first':emp_2.firstname,'last':emp_2.lastname,'position':emp_2.position,'pay':emp_2.salary,'hired':emp_2.hireDate})

# connection.commit()
def displayDatabase():
    print()
    cursor.execute("""SELECT employees.EmployeeID, employees.FirstName, employees.LastName, employees.Position, employees.Salary, employees.HireDate, departments.DepartmentName 
                      FROM employees
                      LEFT JOIN departments ON employees.DepartmentID = departments.DepartmentID 
                      ORDER BY EmployeeID ASC""")
    employees = cursor.fetchall()

    print(f"{'Employee ID':<12}{'First Name':<12}{'Last Name':<12}{'Position':<20}{'Salary':<10}{'Hire Date':<12}{'Department':<15}")
    print("-" * 90)

    for employee in employees:
        employee_id, first_name, last_name, position, salary, hire_date, department = employee
        print(f"{employee_id:<12}{first_name:<12}{last_name:<12}{position:<20}${salary:<10.2f}{hire_date:<12}{department:<15}")
    print()    

def searchForEmployee():
    print("Search by:")
    print("1. Employee ID")
    print("2. First Name")
    print("3. Last Name")
    search_type = input("Choose a search type (1-3): ")

    if search_type == '1':
        print()
        id = input("Type an Id: ")
        print()
        cursor.execute("SELECT * FROM employees WHERE EmployeeID = ?",(id,))
        print(cursor.fetchall())
        connection.commit()
        connection.close()
    elif search_type == '2':
        print()
        firstname = input("Type a Firstname: ")
        print()
        cursor.execute("SELECT * FROM employees WHERE FirstName = ?",(firstname,))
        print(cursor.fetchall())
        connection.commit()
        connection.close()
    elif search_type == '3':
        print()
        lastname = input("Type a LastName: ")
        print()
        cursor.execute("SELECT * FROM employees WHERE LastName = ?",(lastname,))
        print(cursor.fetchall())
        connection.commit()
        connection.close()

def addEmployee():
    print()
    print("Enter the Details of the person you want to add.")
    id = input("Give an ID: ")
    firstname = input("Give a Firstname: ")
    lastname = input("Give a LastName: ")
    position = input("Give a Position: ")
    pay = input("Give Starting Pay ")
    hireDate = input("Give the Date Hired(m/d/yyyy): ")

    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    print("Departments:")
    for dept in departments:
        print(f"{dept[0]}: {dept[1]}")
    dept_id = input("Enter Department ID: ")

    cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?)", (id, firstname, lastname, position, pay, hireDate, dept_id))
    

    print()
    print(f"{firstname},{lastname} Has been added to the Database")
    connection.commit()

def UpdateEmployee():

    displayDatabase()

    print()
    print("What do you want to change?")
    print("1. FirstName")
    print("2. LastName")
    print("3. Position")
    print("4. Pay")
    print("5. Date")
    print("6. Department")
    choice = input("What is your choice: ")

    if choice == '1':
        print()
        id = input("What is the id of the Employee you want to Update: ")
        print()
        firstname = input("What do you want to change the firstName to: ")
        cursor.execute("UPDATE employees SET FirstName = ? WHERE EmployeeID = ?",(firstname,id))
        
 
    elif choice == '2':
        print()
        id = input("What is the id of the Employee you want to Update: ")
        print()
        lastname = input("What do you want to change the lastName to: ")
        cursor.execute("UPDATE employees SET LastName = ? WHERE EmployeeID = ?",(lastname,id))
        

    elif choice == '3':
        print()
        id = input("What is the id of the Employee you want to Update: ")
        print()
        position = input("What do you want to change the position to: ")
        cursor.execute("UPDATE employees SET Position = ? WHERE EmployeeID = ?",(position,id))
         

    elif choice == '4':
        print()
        id = input("What is the id of the Employee you want to Update: ")
        print()
        salary = input("What do you want to change the Salary to: ")
        cursor.execute("UPDATE employees SET Salary = ? WHERE EmployeeID = ?",(salary,id))
        

    elif choice == '5':
        print()
        id = input("What is the id of the Employee you want to Update: ")
        print()
        date = input("What do you want to change the Hire Date to: ")
        cursor.execute("UPDATE employees SET HireDate = ? WHERE EmployeeID = ?",(date,id))

    elif choice == '6':
        print()
        id = input("What is the ID of the Employee you want to update: ")
        print()
        dept_id = input("Enter the new Department ID: ")
        cursor.execute("UPDATE employees SET DepartmentID = ? WHERE EmployeeID = ?", (dept_id, id))
        

    connection.commit()
    print()
    print("Your change has been made.")

def DeleteEmployee():
    print()
    displayDatabase()
    print()    
    id = input("What is the ID of the Employee you want to delete: ")
    cursor.execute("DELETE FROM employees WHERE EmployeeID = ?",(id,))
    print()
    print("it has been Deleted")

def Main():
    running = True
    while running:
        print()
        print("Welcome to the Employee Manager Database")
        print("1. Display Database")
        print("2. Search Employees")
        print("3. Add Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("What would you like to do? ")

        if choice == '1':
            displayDatabase()
        elif choice == '2':
            searchForEmployee()
        elif choice == '3':
            addEmployee()
        elif choice == '4':
            UpdateEmployee()
        elif choice == '5':
            DeleteEmployee()
        elif choice == '6':
            running = False
        else: 
            print("Not a valid choice")

Main()