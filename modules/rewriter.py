import re
import random

WEAK_PHRASES = {
    "worked on": "Engineered and optimized",
    "helped with": "Collaborated on the development of",
    "responsible for": "Spearheaded and managed",
    "did": "Executed and delivered",
    "managed to": "Successfully achieved",
    "was part of": "Contributed to",
    "made": "Designed and implemented",
    "created": "Architected and developed",
    "tried to": "Initiated efforts to",
    "used": "Leveraged"
}

METRICS = [
    "improving overall efficiency by 25%.",
    "resulting in a 15% increase in system performance.",
    "reducing processing time by 30%.",
    "which scaled to support over 10,000 active users.",
    "delivering the project 2 weeks ahead of schedule.",
    "cutting operational costs by 20%.",
    "boosting user engagement by 40%.",
    "achieving 99.9% uptime."
]

def analyze_bullets(resume_text):
    # Split by newlines, try to find bullet-like lines or lines that look like experience sentences
    lines = [line.strip() for line in resume_text.split('\n') if len(line.strip()) > 15]
    
    # Filter to actual bullet points if they exist, otherwise take any short paragraph sentence
    bullets = [line for line in lines if line.startswith('-') or line.startswith('•') or line.startswith('*')]
    if not bullets:
        # Fallback to standard sentences
        bullets = lines
        
    suggestions = []
    
    for bullet in bullets:
        # Strip bullet chars
        clean_bullet = re.sub(r'^[-•*]\s*', '', bullet)
        bullet_lower = clean_bullet.lower()
        
        found_issue = False
        rewritten = clean_bullet
        
        # 1. Check for weak phrases
        for weak, strong in WEAK_PHRASES.items():
            if weak in bullet_lower:
                # Naive replace
                pattern = re.compile(re.escape(weak), re.IGNORECASE)
                rewritten = pattern.sub(strong, rewritten)
                found_issue = True
                
        # 2. Check for missing metrics
        has_metrics = bool(re.search(r'\d', clean_bullet)) or '%' in clean_bullet
        if not has_metrics:
            found_issue = True
            # Append a realistic-sounding metric
            metric = random.choice(METRICS)
            # Add comma if necessary
            if not rewritten.endswith(','):
                rewritten = rewritten.rstrip('.') + ", " + metric
            else:
                rewritten = rewritten + " " + metric
                
        # If the bullet was too short (under 5 words), it's definitely weak
        word_count = len(clean_bullet.split())
        if word_count < 5:
            found_issue = True
            rewritten = f"Designed and executed {clean_bullet.lower()}, " + random.choice(METRICS)
                
        if found_issue:
            # Capitalize first letter safely
            if len(rewritten) > 0:
                rewritten = rewritten[0].upper() + rewritten[1:]
                
            suggestions.append({
                "original": bullet,
                "issue": "Weak action verb or missing quantifiable metrics." if not has_metrics else "Contains weak or passive terminology.",
                "suggestion": rewritten
            })
            
    # Guarantee at least 5 suggestions if we have enough lines
    # If we didn't find enough "bad" ones, let's take some random lines and enhance them anyway
    if len(suggestions) < 5 and len(bullets) > 0:
        remaining = [b for b in bullets if not any(s['original'] == b for s in suggestions)]
        for b in remaining:
            if len(suggestions) >= 5:
                break
            clean_b = re.sub(r'^[-•*]\s*', '', b)
            enhanced = f"Spearheaded initiatives involving {clean_b.lower().rstrip('.')}, " + random.choice(METRICS)
            suggestions.append({
                "original": b,
                "issue": "Could be more impactful and metric-driven.",
                "suggestion": enhanced[0].upper() + enhanced[1:] if len(enhanced) > 0 else enhanced
            })
            
    return suggestions[:5]
