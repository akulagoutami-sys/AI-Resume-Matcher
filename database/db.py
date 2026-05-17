import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'resume_matcher.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# User CRUD
def create_user(name, email, password_hash, role='user'):
    conn = get_connection()
    try:
        conn.execute('INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)',
                     (name, email, password_hash, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_email(email):
    conn = get_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()
    return user

# Analysis CRUD
def save_analysis(user_id, resume_filename, job_title, ats_score, match_pct, matched_skills, missing_skills):
    conn = get_connection()
    conn.execute('''
        INSERT INTO analyses (user_id, resume_filename, job_title, ats_score, match_pct, matched_skills, missing_skills)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, resume_filename, job_title, ats_score, match_pct, matched_skills, missing_skills))
    conn.commit()
    conn.close()

def get_analyses_by_user(user_id):
    conn = get_connection()
    analyses = conn.execute('SELECT * FROM analyses WHERE user_id = ? ORDER BY created_at DESC', (user_id,)).fetchall()
    conn.close()
    return analyses
