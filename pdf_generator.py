# pdf_generator.py
from fpdf import FPDF
from datetime import datetime

class NumerologyPDF(FPDF):
    def header(self):
        # Elegant header line on every page
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(120, 120, 120)
        # FIXED: Removed 'ord' and correctly set layout text alignment
        self.cell(0, 10, "COSMICVIBE AI -- PYTHAGOREAN NUMEROLOGY REPORT", align="L")
        self.ln(12)

    def footer(self):
        # Page numbers on the bottom right
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "R")

def create_numerology_pdf(full_name: str, birth_date: str, reading_text: str) -> bytes:
    """Generates an elegant, structured PDF and returns its raw binary bytes."""
    pdf = NumerologyPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- Cover Title Block ---
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(40, 30, 80) # Royal Spiritual Purple
    pdf.cell(0, 15, "Your Cosmic Blueprint", ln=True, align="L")
    
    pdf.set_font("Helvetica", "I", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, f"Prepared on {datetime.today().strftime('%B %d, %Y')}", ln=True, align="L")
    pdf.ln(10)
    
    # --- User Metadata Box ---
    pdf.set_fill_color(245, 242, 253) # Light lavender wash background
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, f"  FULL NAME: {full_name.upper()}", ln=True, fill=True)
    pdf.cell(0, 8, f"  DATE OF BIRTH: {birth_date}", ln=True, fill=True)
    pdf.ln(12)
    
    # --- Main Content Core ---
    pdf.set_text_color(40, 40, 40)
    
    # Clean up emojis and markdown formatting inconsistencies before passing to PDF layout
    clean_text = reading_text.replace("**", "").replace("### ", "").replace("## ", "").replace("---", "")
    
    # Ensure text is clean ASCII/Latin-1 standard to avoid encoding errors in standard FPDF fonts
    clean_text = clean_text.encode('latin-1', 'replace').decode('latin-1')
    
    for line in clean_text.split("\n"):
        if not line.strip():
            pdf.ln(4)
            continue
            
        # Dynamically highlight header sections within the stream text
        if line.startswith("#") or "RULING NUMBER" in line.upper() or "ARROW" in line.upper() or "MATRIX" in line.upper() or "DESTINY" in line.upper() or "SOUL" in line.upper() or "PERSONALITY" in line.upper():
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(70, 40, 130)
            pdf.ln(4)
            pdf.multi_cell(0, 8, line.replace("#", "").strip())
            pdf.ln(2)
        else:
            # Standard structural paragraph block layout
            pdf.set_font("Helvetica", "", 10.5)
            pdf.set_text_color(50, 50, 50)
            pdf.multi_cell(0, 6, line.strip())
            
    # Return the clean generated stream document directly as byte objects back to Streamlit
    return pdf.output()
