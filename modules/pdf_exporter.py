from fpdf import FPDF

def generate_pdf_report(ats_score, match_level, matched_skills, missing_skills, roadmap):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 15, "AI Resume Analysis Report", 0, 1, "C")
    
    pdf.set_font("Arial", "B", 14)
    pdf.ln(10)
    pdf.cell(0, 10, f"Overall ATS Score: {ats_score} / 100", 0, 1)
    pdf.cell(0, 10, f"Match Level: {match_level}", 0, 1)
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Strengths (Matched Skills):", 0, 1)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, ", ".join(matched_skills) if matched_skills else "None")
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Weaknesses (Missing Skills):", 0, 1)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, ", ".join(missing_skills) if missing_skills else "None")
    
    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Career Roadmap Next Steps:", 0, 1)
    pdf.set_font("Arial", "", 11)
    for step in roadmap:
        if not isinstance(step, str):
            pdf.multi_cell(0, 8, f"Step {step['step']}: {step['topic']} - {step['action']}")
            
    try:
        return pdf.output(dest="S").encode("latin-1")
    except AttributeError:
        return bytes(pdf.output())
