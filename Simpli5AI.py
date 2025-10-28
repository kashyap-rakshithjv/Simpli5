import streamlit as st
import google.generativeai as genai
import os

# --- CONFIGURATION ---
# You can either set the key here or in Streamlit Cloud Secrets
# os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- APP UI ---
st.set_page_config(page_title="Simpli5 AI", page_icon="5️⃣", layout="centered")

st.title("Simpli5 AI")
st.write("Enter a complex topic, and I'll explain it simply — like you're 5 years old!")

# --- INPUT ---
topic = st.text_input("Enter a topic:")

# --- MODEL INITIALIZATION ---
model = genai.GenerativeModel("gemini-2.5-flash")

# --- BUTTON ACTION ---
if st.button("Simplify"):
    if topic.strip() == "":
        st.warning("Please enter a topic before clicking Simplify!")
    else:
        with st.spinner("Thinking..."):
            prompt = f"""
            Explain the following topic in a simple and fun way as if you were teaching a five-year-old.
            Use short sentences, easy words, and engaging examples.

            Topic: {topic}
            """
            response = model.generate_content(prompt)

            st.subheader("Here's your simplified explanation:")
            st.write(response.text)


