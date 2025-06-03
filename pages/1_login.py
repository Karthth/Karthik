import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.database import verify_login

#set up page
st.set_page_config(page_title="Employee Management System - Login", page_icon="🔐")

#show title
st.title("Employee Management System")
st.subheader("Login")

#Create login form
with st.form("login_form"):
    #Input fields
    emp_code = st.text_input("Employee Code")
    password = st.text_input("Password", type="password")

    #login button 
    submit = st.form_submit_button("Login")

    #check login buton is clicked
    if submit:
        #Check if fields are filled
        if emp_code and password:
            # Try to login 
            success,message = verify_login(emp_code,password)

            if success:
                st.success(message)
                #Save login info
                st.session_state['logged_in'] = True
                st.session_state['emp_code'] = emp_code
                #Go to dashboard
                st.switch_page("pages/2_dashboard.py")
            else:
                st.error(message)
        else:
            st.warning("Please enter both employee code and password.")


