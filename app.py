import os
import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Set the OpenAI API key directly in the script
os.environ["OPENAI_API_KEY"] = api_key

# Document Loader
try:
    loader = TextLoader("data.txt", encoding="utf-8")
    loader.load()
except UnicodeDecodeError as e:
    st.error(f"UnicodeDecodeError: {e}")
    # Handle the error or specify how to handle it, such as changing the encoding or replacing characters

# Indexes
index = VectorstoreIndexCreator().from_loaders([loader])

st.title("US Constitution - Chatbot")

query = st.text_input("Enter your question:")
if st.button("Search"):
    results = index.query(query)
    st.write(results)
