import streamlit as st
import google.generativeai as genai

# Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="GenAI Resume Generator")

st.title("🤖 GenAI Resume & Cover Letter Generator")
st.write("Powered by Google Gemini (Generative AI)")

name = st.text_input("Your Name")
role = st.text_input("Target Job Role")
skills = st.text_area("Your Skills (comma separated)")
experience = st.text_area("Your Experience")

if st.button("Generate Content"):
    if name and role and skills and experience:
        prompt = f"""
        You are an expert career coach.

        Generate:
        1. Resume summary
        2. Cover letter
        3. LinkedIn About section

        Name: {name}
        Job Role: {role}
        Skills: {skills}
        Experience: {experience}
        """

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        st.subheader("✨ Generated Output")
        st.write(response.text)
    else:
        st.warning("Please fill all fields.")
