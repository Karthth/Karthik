import mysql.connector

#Simple function tu connect to database 
def get_db_connection():
    try:
        #connect to MySQL database 
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user="root",
            password="12345678",
            database="kar"
        )
        return connection
    except:
        print("Could not connect to database")
        return None
    
# Check if login is correct 
def verify_login(emp_code,password):
    # Get databse connection 
    conn = get_db_connection()
    if not conn:
        return False,"Database connection failed "
    
    try:
        # Create cursor and check login
        cursor = conn.cursor()
        cursor.execute("SELECT employee_code, password FROM kar.karthik WHERE employee_code = %s", (emp_code,))
        result = cursor.fetchone()

        # Close databse connection
        cursor.close()
        conn.close()

        #Check if login is correct
        if result is None:
            return False, "Employee not found"
        elif emp_code == result[0] and password == result[1]:
            return True, "Login Successful"
        else:
            return False, "Wrong password"

    except:
        return False, "Error checking login"

# Get list of all employees
def get_all_employees():
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM kar.karthik")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees
    except:
        return []

#add new employee
def add_employee(emp_code,name,password,deparment):
    conn =get_db_connection()
    if not conn:
        return False,"Database connection failed" 

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO kar.karthik (employee_code,name,password,designation) VALUES (%s,%s,%s,%s)",
            (emp_code,name,password,deparment)

        )
        conn.commit()
        cursor.close()
        conn.close()
        return True,"Employee added successfully"
    except:
        return False, "Error adding employee"

#Update employee details
def update_employee(emp_code,password,designation):
    conn = get_db_connection()
    if not conn:
        return False, "Database connection failed"

    try:
        cursor=conn.cursor()
        cursor.execute(
            "UPDATE kar.karthik SET name =%s, password = %s, designation = %s WHERE employee_code=%s",
        (name,password,designation,emp_code)
        )    
        conn.commit()
        cursor.close()
        conn.close()
        return True,"Employee updated successfully"
    except:
        return False,"Error updating employee"
    
#Delete employee
def delete_employee(emp_code):
    conn =get_db_connection()
    if not conn:
        return False,"Databse connection failed"

    try:
        cursor =conn.cursor()
        cursor.execute("DELETE FROM kar.karthik WHERE employee_code = %s",(emp_code))
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Employee deleted succesfully"
    except:
        return False, "Error deleting employee"












