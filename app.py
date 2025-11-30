import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()


# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

def generate_roadmap(name, experience, target_role, career_goal):
    prompt = f"""
    Create a detailed career roadmap for {name} with {experience} experience in the field of {target_role}. Career goal:{career_goal}.
    Include skills, responsibilities, and career progression steps.
    """
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Career Roadmap")
st.header("AI-Powered Student Career Roadmap Generator")

name = st.text_input("Name")
experience = st.selectbox("Experience Level", ["Entry Level", "Mid Level", "Senior Level"])
target_role = st.text_input("Target Role")
career_goal = st.text_area("Career Goal")

if st.button("Generate Roadmap"):
    if not name or not target_role or not career_goal:
        st.warning("Please fill in all the fields (Name, Target Role, Career Goal) to generate the roadmap.")
    else:
        with st.spinner("Generating..."):
            roadmap = generate_roadmap(name, experience, target_role, career_goal)
        st.markdown(roadmap)
