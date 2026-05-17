def generate_roadmap(target_role, missing_skills):
    if not missing_skills:
        return [{"step": 1, "topic": "Interview Prep", "duration": "Ongoing", "action": "You are fully equipped for this role! Focus on building advanced projects and preparing for interviews."}]
        
    roadmap = []
    
    for i, skill in enumerate(list(missing_skills)[:3]):
        roadmap.append({
            "step": i + 1,
            "topic": skill,
            "duration": "2-4 weeks",
            "action": f"Complete a foundational course in {skill} and build one mini-project using it."
        })
        
    if len(missing_skills) > 3:
        roadmap.append({
            "step": 4,
            "topic": "Continuous Learning",
            "duration": "Ongoing",
            "action": f"After mastering the basics, focus on these remaining skills: {', '.join(list(missing_skills)[3:])}"
        })
        
    return roadmap
