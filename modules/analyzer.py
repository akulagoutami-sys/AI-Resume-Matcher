import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure NLTK data is downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

COMMON_SKILLS = [
    "python", "java", "c++", "c#", "javascript", "typescript", "html", "css", "react", 
    "angular", "vue", "node.js", "express", "django", "flask", "fastapi", "spring boot",
    "sql", "mysql", "postgresql", "mongodb", "nosql", "aws", "azure", "gcp", "docker", 
    "kubernetes", "git", "github", "gitlab", "ci/cd", "jenkins", "machine learning", 
    "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "scikit-learn", 
    "pandas", "numpy", "matplotlib", "seaborn", "data analysis", "data science", 
    "artificial intelligence", "agile", "scrum", "kanban", "communication", "leadership", 
    "problem solving", "teamwork", "project management", "rest api", "graphql", "linux", 
    "bash", "shell scripting", "excel", "tableau", "power bi"
]

def preprocess_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

def extract_skills(text):
    text_lower = text.lower()
    found_skills = set()
    for skill in COMMON_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            formatted_skill = skill.title() if len(skill) > 3 else skill.upper()
            if formatted_skill == "Node.Js": formatted_skill = "Node.js"
            if formatted_skill == "Ci/Cd": formatted_skill = "CI/CD"
            found_skills.add(formatted_skill)
    return found_skills

def calculate_similarity(resume_text, job_description):
    processed_resume = preprocess_text(resume_text)
    processed_jd = preprocess_text(job_description)
    
    if not processed_resume or not processed_jd:
        return 0.0
        
    documents = [processed_resume, processed_jd]
    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform(documents)
    except ValueError:
        return 0.0
    
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0] * 100
