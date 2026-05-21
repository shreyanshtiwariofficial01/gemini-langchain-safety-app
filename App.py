import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Gemini Safety App",
    page_icon="🤖"
)

st.title("🤖 Gemini Safety Test App")

# API KEY
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Direct fallback key
if not gemini_api_key:
    gemini_api_key="AIzaSyDCunHk5KZdNcypPcQEGDwmWwF8zYS2AgU"

os.environ["GOOGLE_API_KEY"] = gemini_api_key

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",

    safety_settings={
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_MEDIUM_AND_ABOVE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_MEDIUM_AND_ABOVE",
        "HARM_CATEGORY_HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_MEDIUM_AND_ABOVE",
    }
)

# Input Box
user_input = st.text_input("Ask something:")

# Button
if st.button("Generate Response"):

    if not user_input.strip():
        st.warning("Please enter a question.")

    else:
        try:
            response = llm.invoke(user_input)

            st.success("Response Generated ✅")

            st.write(response.content)

        except Exception as e:
            st.error(f"Error: {e}")