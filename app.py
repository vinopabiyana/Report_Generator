import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO

# Helper to avoid Unicode crash
def safe_text(text):
    return str(text).encode("latin-1", "replace").decode("latin-1")

# PDF Generator
def generate_pdf(template_choice, df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    # Header based on template
    if template_choice == "Modern":
        pdf.set_text_color(0, 102, 204)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(200, 10, safe_text("Modern Real Estate Report"), ln=True, align="C")
    elif template_choice == "Classic":
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(200, 10, safe_text("Classic Real Estate Report"), ln=True, align="C")
    elif template_choice == "Minimal":
        pdf.set_text_color(100, 100, 100)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(200, 10, safe_text("Minimal Real Estate Report"), ln=True, align="C")

    pdf.ln(10)

    # Table header
    pdf.set_font("Helvetica", "B", 12)
    for col in df.columns:
        pdf.cell(40, 10, safe_text(col), 1, align="C")
    pdf.ln()

    # Table rows
    pdf.set_font("Helvetica", "", 12)
    for _, row in df.iterrows():
        for value in row:
            pdf.cell(40, 10, safe_text(value), 1)
        pdf.ln()

    # Save to buffer
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer


# Streamlit UI
st.title("🏡 Real Estate Report Generator")

uploaded_file = st.file_uploader("Upload a Real Estate CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data", df.head())

    template_choice = st.selectbox(
        "Choose a Report Template",
        ["Modern", "Classic", "Minimal"]
    )

    if st.button("Generate PDF Report"):
        pdf_file = generate_pdf(template_choice, df)
        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_file,
            file_name="real_estate_report.pdf",
            mime="application/pdf"
        )
