import re

WEAK_PHRASES = ["worked on", "helped with", "responsible for", "did", "managed to"]

def analyze_bullets(resume_text):
    # Very crude bullet extractor
    bullets = [line.strip() for line in resume_text.split('\n') if line.strip().startswith('-') or line.strip().startswith('•')]
    
    suggestions = []
    for bullet in bullets:
        bullet_lower = bullet.lower()
        
        # Check for weak phrases
        for weak in WEAK_PHRASES:
            if weak in bullet_lower:
                suggestions.append({
                    "original": bullet,
                    "issue": f"Contains weak phrase '{weak}'",
                    "suggestion": "Start with a strong action verb (e.g., Developed, Spearheaded) and include a quantifiable metric."
                })
                break
                
        # Check for lack of numbers (metrics)
        if not re.search(r'\d', bullet):
            suggestions.append({
                "original": bullet,
                "issue": "Lacks quantifiable results",
                "suggestion": "Add numbers, percentages, or data to demonstrate impact."
            })
            
    return suggestions[:5] # Limit to 5 suggestions
