import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

import os
os.environ['GOOGLE_API_KEY'] = "AIzaSyAHKH8ypLMmST25bhmZ8zar_03QuBBoGIk"

# Initialize the LLM
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Streamlit UI
st.title("Simpli5 AI")
st.write("Enter a complex topic, and I'll simplify it like how I'd do it for a 5-year-old!")

topic = st.text_input("Enter a topic:")

if st.button("Simplify"):
    if topic:
        # Create the prompt manually
        prompt = f"""
        Explain the following topic in a simple way as if you were teaching a ten-year-old.
        Use easy words, short sentences, and fun examples to make it engaging.

        Topic: {topic}
        """
        
        # Format the prompt as a list of messages
        messages = [{"role": "user", "content": prompt}]
        
        # Use the correct method to generate a response
        response = gemini_model.generate(messages)
        
        # Display the simplified explanation
        st.subheader("Here's your simplified explanation:")
        st.write(response)
    else:
        st.warning("Please enter a topic before clicking Simplify!")
