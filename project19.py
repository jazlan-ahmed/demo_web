import streamlit as st

st.set_page_config("Digital Resume")
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Jazlan Ahmed")
    st.write('---')

st.subheader("Summary")
st.write("""
    -I am a passionate software developer with experience in python, 
    web development, and data scientist.  
    -I love creating innovative solutions to complex problems.
         """)
st.write("--------------------------")

st.subheader("Skills")
st.write("-Python")
st.write("-Web Development(HTML,CSS,Javascript.)")
st.write("--------------------------")

st.subheader("Education")
st.write("-BSc in computer science, University of sindh.")
st.write("-2019-2023")
st.write("-Graduated with honors")
st.write("--------------------------")

st.subheader("Projects")
st.write("-Performed exploratory data analysis and built predictive models using Python.")
st.write("-Data Analysis on XYZ dataset.")
st.write("--------------------------")

st.subheader("Contact Information")
st.write("jazlanahmed48@gmail.com")
st.write("www.linkedin.com/in/JazlanAhmed")

with col2:
    st.image("WhatsApp Image 2024-08-09 at 1.13.11 AM.jpeg", width=150)


st.write("---")
st.write("Thank You for viewing my digital resume! feel free to reach out if you'd like to connect.")
