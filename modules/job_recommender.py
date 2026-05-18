ROLE_MAPPINGS = {
    "Data Scientist": ["python", "machine learning", "statistics", "sql", "pandas", "numpy", "data analysis"],
    "Software Engineer": ["java", "python", "c++", "data structures", "algorithms", "git", "sql"],
    "Frontend Developer": ["javascript", "html", "css", "react", "vue", "angular", "ui/ux"],
    "Backend Developer": ["python", "java", "node.js", "sql", "postgresql", "api", "aws"],
    "DevOps Engineer": ["aws", "docker", "kubernetes", "ci/cd", "linux", "bash", "jenkins"],
    "ML Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "aws"]
}

def recommend_jobs(resume_skills):
    recommendations = []
    resume_skills_lower = {s.lower() for s in resume_skills}
    k
    for role, role_skills in ROLE_MAPPINGS.items():
        role_skills_set = set(role_skills)
        matched = role_skills_set.intersection(resume_skills_lower)
        missing = role_skills_set - resume_skills_lower
        
        match_pct = (len(matched) / len(role_skills_set)) * 100 if role_skills_set else 0
        
        if match_pct > 0:
            recommendations.append({
                "role": role,
                "match_pct": int(match_pct),
                "matched_skills": list(matched),
                "missing_skills": list(missing)
            })
            
    # Sort by highest match percentage
    recommendations.sort(key=lambda x: x['match_pct'], reverse=True)
    return recommendations[:3] # Return top 3
