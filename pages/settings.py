import streamlit as st

st.title("⚙️ Settings")

with st.container(border=True):
    st.subheader("Account Preferences")
    st.write("Coming soon...")
    st.toggle("Enable Dark Mode", value=True, disabled=True)
    st.toggle("Email Notifications", value=False)
    
    st.divider()
    
    st.subheader("Danger Zone")
    st.button("Delete Account", type="primary", disabled=True)
