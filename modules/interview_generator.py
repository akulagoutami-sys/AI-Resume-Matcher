import random

TECHNICAL_BANK = {
    "python": [
        {"q": "What is list comprehension in Python?", "hint": "A concise way to create lists using brackets, e.g., [x for x in iterable]."},
        {"q": "What are decorators in Python?", "hint": "Functions that modify the functionality of another function, denoted by @."},
        {"q": "Explain the GIL (Global Interpreter Lock).", "hint": "A mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once."}
    ],
    "java": [
        {"q": "What is the difference between an interface and an abstract class?", "hint": "Interfaces only have abstract methods (pre-Java 8), while abstract classes can have implemented methods and state."},
        {"q": "Explain Garbage Collection in Java.", "hint": "Automatic memory management process that frees up memory by deleting unreachable objects."}
    ],
    "sql": [
        {"q": "Explain the difference between INNER JOIN and LEFT JOIN.", "hint": "INNER returns only matches; LEFT returns all from left table plus matches from right."},
        {"q": "What is the difference between WHERE and HAVING?", "hint": "WHERE filters rows before aggregation; HAVING filters groups after aggregation."}
    ],
    "machine learning": [
        {"q": "Explain overfitting vs underfitting.", "hint": "Overfitting captures noise (too complex); underfitting misses the trend (too simple)."},
        {"q": "What is the bias-variance tradeoff?", "hint": "The balance between a model's ability to minimize bias (error from erroneous assumptions) and variance (error from sensitivity to small fluctuations)."}
    ],
    "aws": [
        {"q": "Difference between EC2 and Lambda?", "hint": "EC2 is an IaaS virtual server; Lambda is a serverless compute service that runs code in response to events."},
        {"q": "What is an S3 bucket?", "hint": "A public cloud storage resource available in AWS, similar to file folders."}
    ],
    "react": [
        {"q": "What are React Hooks?", "hint": "Functions that let you 'hook into' React state and lifecycle features from function components."},
        {"q": "Explain the Virtual DOM.", "hint": "A lightweight copy of the real DOM in memory; React uses it to optimize updates."}
    ],
    "javascript": [
        {"q": "Explain event delegation.", "hint": "Attaching a single event listener to a parent element to manage events for its children."},
        {"q": "What are Promises?", "hint": "Objects representing the eventual completion (or failure) of an asynchronous operation."}
    ],
    "docker": [
        {"q": "Docker image vs container?", "hint": "An image is a read-only template; a container is a running instance of an image."},
        {"q": "What is a Dockerfile?", "hint": "A text document containing commands to assemble an image."}
    ]
}

GENERIC_TECHNICAL = [
    {"q": "How do you ensure your code is secure and optimized?", "hint": "Mention code reviews, static analysis tools, caching, and algorithmic efficiency."},
    {"q": "Describe a complex technical problem you solved.", "hint": "Use the STAR method: Situation, Task, Action, Result."},
    {"q": "How do you handle technical debt?", "hint": "Discuss prioritizing refactoring alongside feature development and communicating risks."}
]

HR_QUESTIONS = [
    {"q": "Where do you see yourself in 5 years?", "hint": "Align your personal growth goals with the company's trajectory."},
    {"q": "Why do you want to work for this company?", "hint": "Demonstrate knowledge of their products, culture, or recent news."},
    {"q": "What is your expected salary?", "hint": "Provide a well-researched range based on market rates and your experience."}
]

BEHAVIORAL_QUESTIONS = [
    {"q": "Tell me about a time you disagreed with a coworker.", "hint": "Focus on communication, empathy, and professional resolution."},
    {"q": "Describe a time you failed and what you learned.", "hint": "Own the mistake, explain the root cause, and detail the actionable steps taken to improve."},
    {"q": "Tell me about a time you had to learn a new technology under pressure.", "hint": "Highlight your adaptability and learning strategy (e.g., reading docs, building POCs)."}
]

PROJECT_QUESTIONS = [
    {"q": "Walk me through the architecture of your most recent project.", "hint": "Explain the frontend, backend, database, and hosting choices."},
    {"q": "What was the most challenging bug you fixed in a recent project?", "hint": "Detail the debugging process and tools used."},
    {"q": "How did you measure the success of your project?", "hint": "Mention KPIs, user feedback, or performance metrics."}
]

def generate_interview_questions(matched_skills, missing_skills, resume_text, job_description):
    questions = []
    seen_qs = set()
    
    def add_q(category, skill, q_dict):
        if q_dict['q'] not in seen_qs:
            questions.append({
                "category": category,
                "skill": skill,
                "question": q_dict['q'],
                "hint": q_dict['hint']
            })
            seen_qs.add(q_dict['q'])

    # 1. Skill-specific Technical Questions (from matched and missing)
    all_skills = list(matched_skills) + list(missing_skills)
    random.shuffle(all_skills)
    
    for skill in all_skills:
        skill_lower = skill.lower()
        if skill_lower in TECHNICAL_BANK:
            for q_dict in TECHNICAL_BANK[skill_lower]:
                add_q("Skill-specific", skill, q_dict)
        else:
            # Generate a dynamic generic question for the skill
            add_q("Technical", skill, {
                "q": f"How would you approach implementing or scaling a solution using {skill}?",
                "hint": f"Discuss best practices, common architectural patterns, and performance considerations for {skill}."
            })

    # Ensure we don't have too many skill questions, cap at 15
    if len(questions) > 15:
        questions = random.sample(questions, 15)

    # 2. General Technical / Coding
    for q_dict in random.sample(GENERIC_TECHNICAL, min(2, len(GENERIC_TECHNICAL))):
        add_q("Coding / Architecture", "General", q_dict)

    # 3. Project-based (derived from resume length/content presence)
    project_count = min(3, len(PROJECT_QUESTIONS))
    for q_dict in random.sample(PROJECT_QUESTIONS, project_count):
        add_q("Project-based", "Experience", q_dict)

    # 4. HR & Behavioral
    for q_dict in random.sample(HR_QUESTIONS, min(3, len(HR_QUESTIONS))):
        add_q("HR", "General", q_dict)
        
    for q_dict in random.sample(BEHAVIORAL_QUESTIONS, min(4, len(BEHAVIORAL_QUESTIONS))):
        add_q("Behavioral", "Soft Skills", q_dict)

    # 5. Company-style / JD-specific
    jd_words = len(job_description.split())
    if jd_words > 50:
        add_q("Company-style", "Role Specific", {
            "q": "Based on the job description, what do you think will be your primary challenge in this role in the first 30 days?",
            "hint": "Reference specific responsibilities mentioned in the JD and propose an onboarding plan."
        })
        add_q("Company-style", "Role Specific", {
            "q": "How does your past experience uniquely qualify you for the specific requirements of this position?",
            "hint": "Map your past achievements directly to the bullet points in the job description."
        })

    # Shuffle slightly but keep some structure
    random.shuffle(questions)
    
    # Cap total questions between 20-30
    return questions[:25]
