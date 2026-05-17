import bcrypt
import streamlit as st
from database.db import get_user_by_email, create_user

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def login_user(email, password):
    user = get_user_by_email(email)
    if user and check_password(password, user['password_hash']):
        st.session_state['authenticated'] = True
        st.session_state['user_id'] = user['id']
        st.session_state['user_name'] = user['name']
        st.session_state['user_email'] = user['email']
        return True
    return False

def logout_user():
    for key in ['authenticated', 'user_id', 'user_name', 'user_email']:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state['authenticated'] = False

def register_user(name, email, password):
    hashed_pwd = hash_password(password)
    return create_user(name, email, hashed_pwd)

def is_authenticated():
    return st.session_state.get('authenticated', False)
