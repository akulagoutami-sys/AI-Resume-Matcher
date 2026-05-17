def calculate_ats_score(similarity_score, matched_skills, jd_skills, resume_text):
    # Base calculation
    skill_ratio = len(matched_skills) / len(jd_skills) if jd_skills else 1.0
    
    # Keyword match (30 pts)
    keyword_score = min((similarity_score / 100) * 30, 30)
    
    # Skills relevance (25 pts)
    skills_score = skill_ratio * 25
    
    # Formatting quality (15 pts) - crude check for standard sections
    sections = ['experience', 'education', 'skills', 'projects']
    sections_found = sum(1 for section in sections if section in resume_text.lower())
    format_score = (sections_found / len(sections)) * 15
    
    # Action verbs usage (10 pts)
    action_verbs = ['developed', 'managed', 'created', 'led', 'designed', 'built', 'implemented']
    verbs_found = sum(1 for verb in action_verbs if verb in resume_text.lower())
    verb_score = min((verbs_found / 3) * 10, 10)
    
    # Quantifiable achievements (10 pts) - check for numbers or %
    import re
    has_numbers = bool(re.search(r'\d', resume_text))
    has_percent = '%' in resume_text
    quant_score = 0
    if has_numbers: quant_score += 5
    if has_percent: quant_score += 5
        
    # Education match (10 pts)
    edu_terms = ['bachelor', 'master', 'phd', 'degree', 'university', 'college']
    edu_score = 10 if any(term in resume_text.lower() for term in edu_terms) else 0
    
    total_score = keyword_score + skills_score + format_score + verb_score + quant_score + edu_score
    return min(int(total_score), 100)
    
def get_match_level(score):
    if score >= 75:
        return "High", "#2e7d32"
    elif score >= 50:
        return "Medium", "#f57c00"
    return "Low", "#c62828"
