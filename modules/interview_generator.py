INTERVIEW_QUESTIONS = {
    "python": "Explain the difference between a list and a tuple.",
    "java": "What is the difference between an interface and an abstract class?",
    "sql": "Explain the difference between INNER JOIN and LEFT JOIN.",
    "react": "What are React Hooks and why are they used?",
    "aws": "Which AWS services have you used for deploying applications?",
    "machine learning": "Explain the bias-variance tradeoff.",
    "docker": "What is the difference between a Docker image and a container?",
    "javascript": "Explain event delegation in JavaScript.",
    "git": "How do you resolve merge conflicts in Git?",
    "agile": "Describe the ceremonies in a Scrum framework."
}

def generate_interview_questions(missing_skills):
    questions = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        if skill_lower in INTERVIEW_QUESTIONS:
            questions.append({
                "skill": skill,
                "question": INTERVIEW_QUESTIONS[skill_lower],
                "type": "Technical"
            })
        else:
            questions.append({
                "skill": skill,
                "question": f"How would you approach learning {skill} quickly on the job?",
                "type": "Behavioral/Learning"
            })
            
    # Add a standard HR question
    questions.append({
        "skill": "General HR",
        "question": "Tell me about a time you had to learn a new technology under pressure.",
        "type": "HR (STAR Method)"
    })
    
    return questions
