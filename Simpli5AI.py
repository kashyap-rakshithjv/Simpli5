import streamlit as st

from langchain import LLMChain, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import os
os.environ['GOOGLE_API_KEY']  = st.secrets['GOOGLE_API_KEY']

# Define the prompt template
simplify_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    Explain the following topic in a simple way as if you were teaching a ten-year-old.
    Use easy words, short sentences, and fun examples to make it engaging.
    
    Topic: {topic}
    """
)

# Initialize the LLM
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create the chain
simplify_chain = LLMChain(llm=gemini_model, prompt=simplify_prompt)

# Streamlit UI
st.title("Simpli5 AI")
st.write("Enter a complex topic, and I'll simplify it like how I'd do it for a 5-year-old!")

topic = st.text_input("Enter a topic:")

if st.button("Simplify"):
    if topic:
        simplified_explanation = simplify_chain.run({"topic": topic})
        st.subheader("Here's your simplified explanation:")
        st.write(simplified_explanation)
    else:
        st.warning("Please enter a topic before clicking Simplify!")
