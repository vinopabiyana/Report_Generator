from fpdf import FPDF
from io import BytesIO

def generate_pdf(template_choice, df):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Unicode font
    pdf.set_font("DejaVu", size=12)

    # Header
    if template_choice == "Modern":
        pdf.set_text_color(0, 102, 204)
        pdf.cell(200, 10, "🏠 Modern Real Estate Report", ln=True, align="C")
    elif template_choice == "Classic":
        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, "📜 Classic Real Estate Report", ln=True, align="C")
    else:
        pdf.set_text_color(100, 100, 100)
        pdf.cell(200, 10, "✨ Minimal Real Estate Report", ln=True, align="C")

    pdf.ln(10)

    # Table header
    for col in df.columns:
        pdf.cell(40, 10, str(col), 1, align="C")
    pdf.ln()

    # Table rows
    for _, row in df.iterrows():
        for value in row:
            pdf.cell(40, 10, str(value), 1)
        pdf.ln()

    # Save to buffer
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer
