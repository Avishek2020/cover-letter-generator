import streamlit as st
from fpdf import FPDF
from datetime import datetime
# Function to generate the cover letter PDF
def create_pdf(name, company_name, company_address, profile, role, color="blue", font="Arial"):
    pdf = FPDF()
    pdf.add_page()
    
    # Heading in selected color
    #pdf.set_text_color(0, 0, 255)  # Default blue
    if color.lower() == "red":
        pdf.set_text_color(255, 0, 0)
    elif color.lower() == "green":
        pdf.set_text_color(0, 255, 0)
    elif color.lower() == "Purple":
        pdf.set_text_color(128, 0, 128)
    elif color.lower() == "Orange":
        pdf.set_text_color(255, 165, 0)
    elif color.lower() == "Black":
        pdf.set_text_color(0, 0, 0)
        
    # Set the fill color (e.g., light gray)
    pdf.set_fill_color(230, 230, 230)  # RGB color for light gray
    
    pdf.set_font(font, 'B', 17)
    pdf.cell(190, 8, f"Avishek Mishra", ln=True, align='C', fill=True)
    # Add a horizontal line after the contact info
    #pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a horizontal line

    pdf.set_font(font, '', 8)
    # First part: up to the email address
    pdf.cell(190, 4, "Bad-Lippspringe, Germany | +49 17685225808 | avishek2020@gmail.com", ln=True, align='C', fill=True)

    # Second part: after the email address, starting on a new line
    pdf.cell(190, 4, "LinkedIn: linkedin.com/in/avishek2020 | GitHub: github.com/Avishek2020/", ln=True, align='C', fill=True)

   
    # Body of the cover letter
    pdf.set_text_color(0, 0, 0)  # Black color for the text
    pdf.set_font("Arial", '', 12)
    today_date = datetime.today().strftime('%B %d, %Y')
    # Regular font for the date
    pdf.multi_cell(0, 5, f"\n\n\n\n{today_date}\n\n")
    
    # Bold font for the company name and address
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 5, f"{company_name}\n{company_address}\n\n")

    # Regular font for the body
    pdf.set_font("Arial", '', 12)
    
    text = (        
        f"Dear Hiring Manager,\n\n"
        f"I am excited to apply for the {role} position at {company_name}. With over 6 years of experience in software development and 3 years in data "
        f"science and engineering, I am confident in my ability to contribute effectively to your team. I have a strong foundation in software "                   f"engineering,with expertise in Python,Java, C/C++, and Databases (Oracle, Postgresql, MongoDB, MySQL).\n\n"
        
        f"During my master studies in Intelligence and Data in Germany, I focused on advanced neural sequence-to-sequence models like GPT-2 and BART for "         f"my thesis. I developed a Large language model that generates professional qulaity English text from simplified English text inputs, "
        f"which honed my expertise in natural language processing and sharpened my ability to solve complex problems using cutting-edge technology.\n\n"
        
        f"Throughout my career, I have worked on projects involving computer graphics, machine learning, and computer vision. At PRODASO GmbH, where I "           f"have been a data scientist for over 3 years, I have gained valuable experience working with IIoT and IoT data in industries such as healthcare,"         f"manufacturing, and food. My role involved analyzing large datasets, developing predictive models, and delivering insights that informed key"             f"business decisions.\n\n" 
        f"I have demonstrated success in multiple projects and have consistently applied my skills to solve complex problems.\n"
        f"I am passionate about {role} and always look forward to contributing to impactful projects.\n\n"
        f"Thank you for considering my application. I am excited about the possibility of working with {company_name}.\n\n"
        f"Sincerely,\n" 
    )
    pdf.multi_cell(0, 5, text)
    # Bold font for the signature
    pdf.set_font("Arial", 'B', 10)
    pdf.multi_cell(0, 5, f"{name}\n")
    
    pdf.set_y(-33); pdf.set_fill_color(230, 230, 230); pdf.cell(0, 12, '', 0, 1, 'C', fill=True)


    # Save PDF
    pdf_output = f"{name}_cover_letter_{company_name}.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Streamlit UI
st.title("Custom Cover Letter Generator")

name = st.text_input("Enter Your Name", "Avishek Mishra")
company_name = st.text_input("Enter Company Name", "Apple Inc")
company_address = st.text_input("Enter Company Address", "Germany")
profile = st.text_input("Enter Your Profile (e.g., Data Science, Software Development)", "Data Scientist")
role = st.text_input("Enter Role You're Applying For", "Data Scientist")
color = st.selectbox("Choose Heading Color", ["Blue", "Red", "Green", "Purple", "Orange", "Black" ])
font = st.selectbox("Choose Font", ["Arial", "Courier", "Times", "Tahoma"])

if st.button("Generate Cover Letter"):
    pdf_file = create_pdf(name, company_name, company_address, profile, role, color=color, font=font)
    st.success(f"Cover letter created: {pdf_file}")

    # Provide a download button
    with open(pdf_file, "rb") as file:
        st.download_button("Download PDF", data=file, file_name=pdf_file)
