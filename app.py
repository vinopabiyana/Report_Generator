import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO

st.title("📑 Report Generator with Templates")

# Upload Data
uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])

# Template Options
template_choice = st.selectbox("Choose a Template", ["Modern", "Classic", "Minimal"])

# PDF Generator
def generate_pdf(template, data):
    pdf = FPDF()
    pdf.add_page()

    # Add Unicode font (you must have DejaVuSans.ttf in your project folder)
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    # Title based on template
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

    # Add table rows (first 10 rows only for demo)
    for i in range(min(10, len(data))):
        row_text = str(data.iloc[i].to_dict())
        pdf.multi_cell(0, 10, row_text)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    if st.button("Generate Report"):
        pdf_file = generate_pdf(template_choice, df)
        st.download_button(
            label="📥 Download Report",
            data=pdf_file,
            file_name=f"report_{template_choice.lower()}.pdf",
            mime="application/pdf"
        )
