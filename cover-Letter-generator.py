import streamlit as st
from fpdf import FPDF
from datetime import datetime
# Function to generate the cover letter PDF
def create_pdf(name, company_name, company_address, profile, role, color="blue", font="Arial"):
    pdf = FPDF()
    pdf.add_page()
    
    # Heading in selected color
    pdf.set_text_color(0, 0, 255)  # Default blue
    if color.lower() == "red":
        pdf.set_text_color(255, 0, 0)
    elif color.lower() == "green":
        pdf.set_text_color(0, 255, 0)
    
    pdf.set_font(font, 'B', 15)
    pdf.cell(200, 10, f"Avishek Mishra", ln=True, align='C')
    # Add a horizontal line after the contact info
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a horizontal line

    pdf.set_font(font, '', 8)
    # First part: up to the email address
    pdf.cell(200, 3, "Bad-Lippspringe, Germany | +49 17685225808 | avishek2020@gmail.com", ln=True, align='C')

    # Second part: after the email address, starting on a new line
    pdf.cell(200, 3, "LinkedIn: linkedin.com/in/avishek2020 | GitHub: github.com/Avishek2020/", ln=True, align='C')

   
    # Body of the cover letter
    pdf.set_text_color(0, 0, 0)  # Black color for the text
    pdf.set_font("Arial", '', 10)
    today_date = datetime.today().strftime('%B %d, %Y')
    
    text = (
        f"\n{today_date}\n"
        f"{company_name}\n"
        f"{company_address}\n\n"
        f"Dear Hiring Manager,\n\n"
        f"I am writing to express my interest in the {role} position at {company_name}. "
        f"With my experience in {profile}, I believe I would be an excellent fit for your team.\n\n"
        f"I have demonstrated success in multiple projects and have consistently applied my skills to solve complex problems. "
        f"I am passionate about {role} and always look forward to contributing to impactful projects.\n\n"
        f"Thank you for considering my application. I am excited about the possibility of working with {company_name}.\n\n"
        f"Sincerely,\n"
        f"{name}"
    )
    pdf.multi_cell(0, 5, text)

    # Save PDF
    pdf_output = f"{name}_cover_letter_{company_name}.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Streamlit UI
st.title("Custom Cover Letter Generator")

name = st.text_input("Enter Your Name", "Avishek")
company_name = st.text_input("Enter Company Name", "Apple Inc")
company_address = st.text_input("Enter Company Address", "Germany")
profile = st.text_input("Enter Your Profile (e.g., Data Science, Software Development)", "Data Scientist")
role = st.text_input("Enter Role You're Applying For", "Data Scientist")
color = st.selectbox("Choose Heading Color", ["Blue", "Red", "Green"])
font = st.selectbox("Choose Font", ["Arial", "Courier", "Times"])

if st.button("Generate Cover Letter"):
    pdf_file = create_pdf(name, company_name, company_address, profile, role, color=color, font=font)
    st.success(f"Cover letter created: {pdf_file}")

    # Provide a download button
    with open(pdf_file, "rb") as file:
        st.download_button("Download PDF", data=file, file_name=pdf_file)
