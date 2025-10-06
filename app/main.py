import streamlit as st
from src.rag_pipeline import generate_answer

st.title("🚀 SparkGPT – Distributed RAG on Databricks")
query = st.text_input("Ask a question about your documents:")
if st.button("Run Query"):
    answer = generate_answer(query)
    st.success(answer)
