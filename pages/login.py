import streamlit as st
from utils.auth import login_user

st.title("Log in")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Log In", type="primary"):
    if login_user(email, password):
        st.success("Logged in successfully!")
        st.rerun()
    else:
        st.error("Invalid email or password.")
