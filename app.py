import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO

st.title("📑 Report Generator with Templates")

# Upload Data
uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])

# Template Options
template_choice = st.selectbox("Choose a Template", ["Modern", "Classic", "Minimal"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # PDF Generator
    def generate_pdf(template, data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        if template == "Modern":
            pdf.set_text_color(0, 102, 204)  # Blue headings
            pdf.cell(200, 10, "📊 Modern Report", ln=True, align="C")
        elif template == "Classic":
            pdf.set_text_color(0, 0, 0)  # Black text
            pdf.cell(200, 10, "📜 Classic Report", ln=True, align="C")
        elif template == "Minimal":
            pdf.set_text_color(100, 100, 100)
            pdf.cell(200, 10, "✨ Minimal Report", ln=True, align="C")

        pdf.ln(10)
        for i in range(min(10, len(data))):
            pdf.cell(200, 10, txt=str(data.iloc[i].to_dict()), ln=True)

        buffer = BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        return buffer

    if st.button("Generate Report"):
        pdf_file = generate_pdf(template_choice, df)
        st.download_button(
            label="📥 Download Report",
            data=pdf_file,
            file_name=f"report_{template_choice.lower()}.pdf",
            mime="application/pdf"
        )
