def generate_roadmap(target_role, missing_skills):
    """
    Generate a deterministic 6-month career roadmap based on missing skills.
    If less than 6 skills are missing, fallback to general career progression topics.
    """
    missing_list = list(missing_skills) if missing_skills else []
    
    # Fallback skills if user has very few missing skills
    general_topics = [
        "System Design & Architecture",
        "Cloud Deployment (AWS/GCP)",
        "Advanced CI/CD Pipelines",
        "Leadership & Agile Mentoring",
        "Open Source Contribution",
        "Technical Blogging & Portfolio"
    ]
    
    # Pad missing skills list to ensure we always have at least 6 months
    while len(missing_list) < 6:
        topic = general_topics.pop(0)
        if topic not in missing_list:
            missing_list.append(topic)
            
    roadmap = []
    
    for month in range(1, 7):
        skill = missing_list[month - 1]
        
        roadmap.append({
            "month": month,
            "skill": skill,
            "resources": f"Official documentation, Udemy masterclass on {skill}, YouTube crash courses.",
            "project": f"Build a prototype integrating {skill} into a CRUD application.",
            "outcome": f"Proficiency in {skill} suitable for technical interviews."
        })
        
    return roadmap
