import pandas as pd
import io

def generate_excel_report(matched_skills, missing_skills, jobs):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        
        # Balance columns
        len_matched = len(matched_skills)
        len_missing = len(missing_skills)
        max_len = max(len_matched, len_missing)
        
        matched_col = list(matched_skills) + [""] * (max_len - len_matched)
        missing_col = list(missing_skills) + [""] * (max_len - len_missing)
        
        # Sheet 1: Skills
        skills_data = {
            "Matched Skills": matched_col,
            "Missing Skills": missing_col
        }
        df_skills = pd.DataFrame(skills_data)
        df_skills.to_excel(writer, sheet_name="Skill Analysis", index=False)
        
        # Sheet 2: Job Recommendations
        if jobs:
            job_data = {
                "Role": [j['role'] for j in jobs],
                "Match %": [j['match_pct'] for j in jobs],
                "Missing Skills": [", ".join(j['missing_skills']) for j in jobs]
            }
            df_jobs = pd.DataFrame(job_data)
            df_jobs.to_excel(writer, sheet_name="Job Recommendations", index=False)
        else:
            pd.DataFrame({"Note": ["No job recommendations"]}).to_excel(writer, sheet_name="Job Recommendations", index=False)
            
    return output.getvalue()
