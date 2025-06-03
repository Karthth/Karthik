import streamlit as st
from utils.database import get_all_employees, add_employee, update_employee, delete_employee

#Set up the page
st.set_page_config(page_title="Employee management syatem - Manage Employees", page_icon="👥")

#Check if user is logged in 
if 'logged_in' not in st.session_state or not st.session_state or not st.session_state['logged_in']:
    st.warning("Please login first")
    st.stop()

#Show title
st.title("Manage Employees")

#Create tabs for diffrent operations
tab1, tab2, tab3 = st.tabs(["Add Employee","Edit Employee", "Delete Employee"])

#Add Employee tab
with tab1:
    st.subheader("Add New Employee")
    with st.form("add_employee_form"):
        #Input fields
        emp_code= st.text_input("Employee Code")
        name= st.text_input("Full Name")
        password = st.text_input("Password", type="password")
        department = st.selectbox(
            "Department",
            ["IT","HR","Finance","Marketing","Operations"]
        )

        #add button
        submit =st.form_submit_button("Add Employee")
         
        if submit:
           #Check if all fields are filled
           if emp_code and name and password and department:
              success, message = add_employee(emp_code, name,password, department)
              if success:
                  st.success(message)
                  st.rerun()
              else:
                  st.error(message)
           else:
               st.warning("Please fill in all fields.")

# Edit Employee Tab
with tab2:
    st.subheader("Edit Employee")
    
    # Fetch employees inside this tab to avoid state bleed
    employees = get_all_employees()

    if employees:
        # Create dropdown for selecting employee
        employee_options = {f"{emp['employee_code']} - {emp['name']}": emp for emp in employees}
        selected_employee_key = st.selectbox("Select Employee to Edit", options=list(employee_options.keys()))

        if selected_employee_key:
            employee = employee_options[selected_employee_key]

            with st.form("edit_employee_form"):  # Unique form key
                # Input fields with current values
                name_input = st.text_input("Name", value=employee['name'])
                password_input = st.text_input("Password", type="password", value=employee['password'])
                designation_input = st.text_input("Designation", value=employee['designation'])

                update_submit = st.form_submit_button("Update Employee")

                if update_submit:
                    if name_input and password_input and designation_input:
                        success, message = update_employee(employee['employee_code'], name_input, password_input, designation_input)
                        if success:
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.warning("Please fill in all fields.")
    else:
        st.info("No employees found in the database.")


#delete Employee tab
with tab3:
    st.subheader("Delete Employee")
    if employees:
        #Create dropdown for delecting employee
        employee_options={f"{emp['employee_code']} - {emp['name']}":emp for emp in employees}
        selected_employee_key = st.selectbox(
            "Select Employee to delete",
            options=list(employee_options.keys())
        )

        if selected_employee_key:
            employee = employee_options[selected_employee_key]
            # Delete button
            if st.button("Delete Selected Employee"):
                # Check if trying to delete own account
                if st.session_state['emp_code'] == employee['employee_code']:
                    st.error("You cannot delete your own account!")
                else:
                    success, message = delete_employee(employee['employee_code'])
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
    else:
        st.info("No employees found in the database.")

# Add back button
if st.button("Back to Dashboard"):
    st.switch_page("pages/2_dashboard.py")                          

              

            