import streamlit as st
from utils.database import get_all_employees

#set up the page
st.set_page_config(page_title="Employee Management System - Dashboard", page_icon="🔐")

#Check if user is logged in
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please login first")
    st.stop()

# Show title
st.title("Employee Dashboard")
st.subheader("Employee List")

#Get list of employees
employees = get_all_employees()

#Show employee list
if employees:
    #Create simple table
    st.dataframe(
        employees,
        column_config={
            "employee_code": "Employee Code",
            "name": "Name",
            "designation": "Department",
        },
        hide_index=True
    )
else:
    st.info("No employees found in the datbase:")

#Add logout button
if st.button("Logout"):
    #clear login info
    st.session_state.clear()
    #Go back to login page
    st.switch_page("pages/1_Login.py")    