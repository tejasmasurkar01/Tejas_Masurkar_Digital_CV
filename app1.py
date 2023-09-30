from pathlib import Path
import streamlit as st
from PIL import Image

def load_data():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "assets" / "CV.pdf"
    profile_pic = current_dir / "assets" / "Photo.png"
    with open(css_file) as f:
        css_styles = f.read()
    with open(resume_file, "rb") as pdf_file:
        pdf_data = pdf_file.read()
    profile_image = Image.open(profile_pic)
    return css_styles, pdf_data, profile_image

def show_header(profile_image, name, description, email):
    st.image(profile_image, width=230)
    st.title(name)
    st.write(description)
    st.download_button(
        label=" 📄 Download Resume",
        data=pdf_data,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", email)

def show_social_media_links(social_media_links):
    cols = st.columns(len(social_media_links))
    for index, (platform, link) in enumerate(social_media_links.items()):
        cols[index].write(f"[{platform}]({link})")

def show_education():
    st.subheader("Education")
    st.write(
        """
        - 🎓 Bachelor of Engineering 
        - 💻 Branch: Computer Science & Engineering
        - 🏫 College: GH Raisoni College of Engineering Nagpur
        """
    )

def show_experience_qualifications():
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - ✔️ Strong hands-on experience and knowledge in Python and Excel
        - ✔️ Good understanding of statistical principles and their respective applications
        - ✔️ Excellent team-player and displaying a strong sense of initiative on tasks
        """
    )

def show_skills():
    st.subheader("Skills")
    st.write(
        """
        - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
        - 📊 Data Visualization: PowerBi, MS Excel, Plotly
        - 📚 Modeling: Logistic regression, linear regression, decision trees
        - 🗄️ Databases: Postgres, MongoDB, MySQL
        """
    )

def show_projects_accomplishments(projects):
    st.subheader("Projects & Accomplishments")
    for project, details in projects.items():
        st.write(f"- {project}")
        st.write(f"  {details}")

# Main
css_styles, pdf_data, profile_image = load_data()

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.markdown("<style>{}</style>".format(css_styles), unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")
with col1:
    show_header(profile_image, NAME, DESCRIPTION, EMAIL)
with col2:
    show_social_media_links(SOCIAL_MEDIA)

st.write('\n')
show_education()
st.write('\n')
show_experience_qualifications()
st.write('\n')
show_skills()
st.write('\n')
show_projects_accomplishments(PROJECTS)
