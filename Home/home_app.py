import streamlit as st

# Page settings
st.set_page_config(
    page_title="Robert Smales - Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# Header
st.markdown(
    """
    <h1 style='text-align: center; color: #0F4C81;'>Robert Smales</h1>
    <h3 style='text-align: center; color: #2E4057;'>Final-Year Data Science Student</h3>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Introduction
st.markdown(
    """
I am a final-year Data Science student building **interactive dashboards** and **data projects** 
for small businesses. My goal is to turn messy data into actionable insights 
through clear visualizations and predictive analytics.
"""
)

st.write("---")

# Projects section
st.subheader("Projects (Coming Soon)")

st.markdown(
    """
- [Project 1: Sales Dashboard](../Projects/Project1/app.py) – interactive dashboard coming soon  
- [Project 2: Customer Segmentation](../Projects/Project2/app.py) – interactive dashboard coming soon
"""
)

st.write("---")

# Contact section
st.subheader("Contact Me")
st.markdown(
    """
- Email: robert.a.smales@gmail.com  
- GitHub: [https://github.com/Robert-Smales/data-portfolio](https://github.com/Robert-Smales/data-portfolio)  
- LinkedIn: [https://www.linkedin.com/in/robert-smales-b2725b253](https://www.linkedin.com/in/robert-smales-b2725b253)
"""
)

st.write("---")
st.markdown(
    "<p style='text-align: center; color: #AAAAAA;'>© 2026 Robert Smales</p>",
    unsafe_allow_html=True
)
