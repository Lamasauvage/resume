from pathlib import Path
import streamlit as st
from PIL import Image

# Set the page config
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"
page_icon = str(current_dir / "assets" / "doom.png")
ovh_logo = str(current_dir / "assets" / "ovhcloud_logo.jpg")
helpline_logo = str(current_dir / "assets" / "helpline_logo.jpg")

# --- GENERAL SETTINGS ---

PAGE_TITLE = "Digital CV - Guillaume ADAM"
PAGE_ICON = page_icon
NAME = "Guillaume ADAM"
DESCRIPTION = "Junior Developer Python | IT Support Technician"
EMAIL = "adam.guillaume78@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/guillaume-adam-397b36109/",
    "GitHub": "https://github.com/Lamasauvage",
}
PROJECTS = {
    "Complete Website Development Project with Database": "https://acs-sport-santé.fr",
    "Professional Title": "https://www.francecompetences.fr/recherche/rncp/37674/",
    "IT Asset Management and Compliance Automation System": None,
    "🏆 More projects to come...": None,
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbytes = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.markdown(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbytes,
        file_name=resume_file.name,
        mime="application/pdf",
    )
    st.write(" 📬", EMAIL)

# --- SOCIAL MEDIA ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- GOALS ---

st.write("#")
st.subheader("Career Aspirations")
st.markdown(
    """
    <div style="text-align: justify;">
        🌱 As I continue to grow and develop professionally, my goal is to become a Software Developer, 
        specializing in Python. I am passionate about writing clean, efficient, and accessible code.<br><br>
        📊 Additionally, I have a strong interest in the fields of Data Analysis, Data Engineering and AI. 
        <br><br>
        💻 I aspire to leverage my skills in these areas to contribute to meaningful projects that drive 
        business innovation and success. My ideal role is one where I can keep learning, 
        tackle challenging problems, and make a positive impact with my work.<br><br>
        🚀 My future aspirations are not just to grow as a developer but also to contribute significantly 
        to my team and the wider community through innovative solutions and continuous improvement.
    </div>
    """,
    unsafe_allow_html=True
)


# --- EXPERIENCE ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ Over 3 years of experience in IT support and Proximity Helpdesk roles, specializing in incident resolution and proactive maintenance to ensure continuous operations
- ✅ Proficient in setting up and managing diverse operating systems including Windows (10/11), Linux (Ubuntu) and Mac (every version)
- ✅ Experience in the management of IT projects, from the design phase to the implementation of the solution
- ✅ Demonstrated ability to provide comprehensive technical support and troubleshooting in fast-paced environments
- ✅ Excellent communication skills, with the ability to explain technical issues in a simple and understandable way
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 💻 Operating Systems : Windows, Linux, Mac
    - 🌐 Networking : TCP/IP, DNS, DHCP, VLAN, VPN
    - </> Web Development : HTML, CSS, JavaScript, PHP, Symfony, Bootstrap
    - 🔧 Backend Development : Python, Django
    - 🗄️ Database : MySQL, PostgreSQL
    - 🔄 Version Control : Git, GitHub
"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image(ovh_logo, width=100)
with col2:
    st.write("Helpdesk Technician | OVHCloud")
    st.write("12/2019 - Present")

st.write(
    """
- ► Provide technical support to customers on site and remotely
- ► Prepare and manage the deployment of new workstations (Windows, Linux, Mac)
- ► Manage the installation and maintenance of network equipment (switches, routers, network patch panels)
- ► Implement new processes to improve the quality of service and write technical documentation
- ► Manage the inventory of IT equipment and the stock of spare parts
"""
)

# --- SPACE ---
st.write("#")
st.write("---")

# --- JOB 2 ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image(helpline_logo, width=100)
with col2:
    st.write("IT Support Technician | HELPLINE")
    st.write("10/2018 - 11/2019")

st.write(
    """
- ► Provided comprehensive IT support for clients like Keolis and Accor, ensuring efficient resolution of user issues.
- ► Responsible for computer imaging for new users, configuring systems with necessary software, email setup, and network drives.
- ► Managed telephony and video conferencing systems, including COMEX meeting rooms (Webex/CISCO), and set up telecommunication lines.
- ► Prepared and configured mobile devices (iPhone/Samsung) for users and installed new user equipment.
- ► Played a key role in Active Directory account management and rights administration.
- ► Handled a high volume of user calls at Henner (average 150 calls/day), providing immediate incident resolution and maintaining a low backlog.
- ► Involved in the improvement and documentation of IT procedures, contributing to a more streamlined IT support process.
"""
)


# --- PROJECTS & ACCOMPLISHMENTS ---

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    if project == "Professional Title":
        st.markdown("🏆 Obtained Professional Title (TP) - [Web and Mobile Web Developer](https://www.francecompetences.fr/recherche/rncp/37674/) in June 2023", unsafe_allow_html=True)
    elif project == "Complete Website Development Project with Database":
        st.markdown("🏆 Complete Website Development Project with Database - [ACS Sport Santé](https://acs-sport-santé.fr)", unsafe_allow_html=True)
    elif project == "IT Asset Management and Compliance Automation System":
        st.markdown("🏆 IT Asset Management and Compliance Automation System : Developed a data integration and anomaly detection system to streamline IT asset management and compliance.")
    elif link:
        # Display other project names as hyperlinks
        st.markdown(f"[{project}]({link})", unsafe_allow_html=True)
    else:
        # If there's no link, just display the text
        st.write(project)
