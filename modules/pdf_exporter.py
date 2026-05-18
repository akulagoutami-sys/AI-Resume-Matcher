import io
try:
    from fpdf import FPDF
except ImportError:
    pass

def clean_and_wrap_text(text, max_word_len=50):
    if not text:
        return "None"
    text = str(text)
    # Replace unicode quotes and hyphens which commonly break latin-1
    text = text.replace("'", "'").replace('"', '"').replace('“', '"').replace('”', '"')
    text = text.replace('–', '-').replace('—', '-')
    
    # Split ridiculously long words to prevent FPDF 'horizontal space' exception
    words = text.split()
    wrapped_words = []
    for w in words:
        if len(w) > max_word_len:
            # Force split the word into chunks
            chunks = [w[i:i+max_word_len] for i in range(0, len(w), max_word_len)]
            wrapped_words.append(" ".join(chunks))
        else:
            wrapped_words.append(w)
            
    text = " ".join(wrapped_words)
    
    # Encode to latin-1 and ignore bad chars
    return text.encode('latin-1', 'ignore').decode('latin-1')

def generate_pdf_report(ats_score, match_level, matched_skills, missing_skills, roadmap):
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        pdf.set_font("Arial", "B", 20)
        # Using w=190 instead of 0 for strict boundaries
        pdf.cell(190, 15, "AI Resume Analysis Report", ln=1, align="C")
        
        pdf.set_font("Arial", "B", 14)
        pdf.ln(10)
        pdf.cell(190, 10, f"Overall ATS Score: {ats_score} / 100", ln=1)
        pdf.cell(190, 10, f"Match Level: {clean_and_wrap_text(match_level)}", ln=1)
        
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(190, 10, "Strengths (Matched Skills):", ln=1)
        pdf.set_font("Arial", "", 11)
        
        matched_str = ", ".join(matched_skills) if (matched_skills and len(matched_skills) > 0) else "None"
        pdf.multi_cell(190, 8, clean_and_wrap_text(matched_str))
        
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(190, 10, "Weaknesses (Missing Skills):", ln=1)
        pdf.set_font("Arial", "", 11)
        
        missing_str = ", ".join(missing_skills) if (missing_skills and len(missing_skills) > 0) else "None"
        pdf.multi_cell(190, 8, clean_and_wrap_text(missing_str))
        
        pdf.ln(10)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(190, 10, "Career Roadmap Next Steps:", ln=1)
        pdf.set_font("Arial", "", 11)
        
        if roadmap:
            for step in roadmap:
                if isinstance(step, dict):
                    topic = clean_and_wrap_text(step.get('topic', ''))
                    action = clean_and_wrap_text(step.get('action', ''))
                    s_num = step.get('step', '')
                    pdf.multi_cell(190, 8, f"Step {s_num}: {topic} - {action}")
                else:
                    pdf.multi_cell(190, 8, clean_and_wrap_text(str(step)))
        else:
            pdf.multi_cell(190, 8, "No roadmap steps available.")
            
        try:
            return pdf.output(dest="S").encode("latin-1")
        except AttributeError:
            return bytes(pdf.output())
            
    except Exception as e:
        print(f"PDF Generation Error: {e}")
        return b"Error generating PDF. Please check server logs."
