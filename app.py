import streamlit as st
import os

#Set page configuration
st.set_page_config(page_title="Employee Management System", page_icon="💼")

#Display logo
logo_path = os.path.join("artifacts","logo.png")
if os.path.exists(logo_path):
    st.logo(logo_path)


# Switch to login page
st.switch_page("pages/1_login.py") 