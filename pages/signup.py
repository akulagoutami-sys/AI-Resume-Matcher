import streamlit as st
from utils.auth import register_user

st.title("Sign up")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register", type="primary"):
    if password != confirm_password:
        st.error("Passwords do not match.")
    elif not name or not email or not password:
        st.error("Please fill in all fields.")
    else:
        if register_user(name, email, password):
            st.success("Registration successful! You can now log in.")
        else:
            st.error("Email already exists. Please log in.")
