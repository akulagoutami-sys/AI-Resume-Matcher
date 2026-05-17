import streamlit as st

st.title("👤 Profile Settings")

st.write(f"**Name:** {st.session_state.get('user_name')}")
st.write(f"**Email:** {st.session_state.get('user_email')}")

st.info("Profile settings and account deletion will be implemented here.")
