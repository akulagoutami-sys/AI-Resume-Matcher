from sklearn.feature_extraction.text import TfidfVectorizer

def extract_top_keywords(job_description, top_n=15):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    try:
        vectorizer.fit_transform([job_description])
        return vectorizer.get_feature_names_out()
    except ValueError:
        return []

def optimize_keywords(resume_text, job_description):
    top_jd_keywords = extract_top_keywords(job_description)
    resume_lower = resume_text.lower()
    
    found_keywords = []
    missing_keywords = []
    
    for kw in top_jd_keywords:
        if kw in resume_lower:
            found_keywords.append(kw)
        else:
            missing_keywords.append(kw)
            
    return found_keywords, missing_keywords
