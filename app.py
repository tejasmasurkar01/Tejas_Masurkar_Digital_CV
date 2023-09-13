from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Photo.png"


PAGE_TITLE = "Digital CV | Tejas Masurkar"
PAGE_ICON = ":wave:"
NAME = "Tejas Masurkar"
DESCRIPTION = """
Data Analyst
"""
EMAIL = "tejasmasurkar01@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/tejas-masurkar-105b72215/?originalSubdomain=in",
    "GitHub": "https://github.com/tejasmasurkar01",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Education")
st.write(
    """
- 🎓 Bachelor of Engineering 
- 💻 Branch : Computer Science & Engineering
- 🏫 College : GH Raisoni College of Engineering Nagpur
"""
)

st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)



st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


st.write('\n')
st.subheader("Projects & Accomplishments")
st.write(
    """
-✔️ Online Pharmacy Management System(OPMS) Date: Oct 2021

Tools/Technologies Used: JavaScript, HTML, CSS, MySQL

Created an Online Pharmacy Management System (OPMS) utilizing HTML/CSS and MySQL database system, and used WAMP server to host the database.
Users may log in or establish an account, see their purchase history and status, submit orders, and view the prescriptions they have picked in their shopping basket.

-✔️ Fake News Detection using Machine Learning Date: Dec 2020/May 2021

Tools/Technologies Used: Python, NLP, Google Collaboratory

Created a Fake News Classifier to classify news as true or fake with an accuracy of 92.7%.
Implemented Passive Aggressive, Multinomial Naive Bayes Classifiers and NLP.
"""   
    )
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
