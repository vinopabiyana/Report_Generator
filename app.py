from fpdf import FPDF

def generate_pdf(template, data):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Unicode font
    pdf.set_font("DejaVu", size=12)

    if template == "Modern":
        pdf.set_text_color(0, 102, 204)
        pdf.cell(200, 10, "📊 Modern Report", ln=True, align="C")
    elif template == "Classic":
        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, "📜 Classic Report", ln=True, align="C")
    elif template == "Minimal":
        pdf.set_text_color(100, 100, 100)
        pdf.cell(200, 10, "✨ Minimal Report", ln=True, align="C")

    pdf.ln(10)
    for i in range(min(10, len(data))):
        row_text = str(data.iloc[i].to_dict())
        pdf.multi_cell(0, 10, row_text)  # safer than .cell()

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer
