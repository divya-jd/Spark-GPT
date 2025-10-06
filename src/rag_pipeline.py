from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate
from src.vector_store import VectorSearch
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()

embedder = SentenceTransformer("all-MiniLM-L6-v2")
llm = OpenAI(temperature=0.2, model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
retriever = VectorSearch()

prompt_template = """
Context: {context}
Question: {query}
Answer the question concisely using the context.
"""

def generate_answer(query):
    query_vec = embedder.encode(query)
    indices, _ = retriever.search(query_vec)
    context = "Relevant passages from docs"
    chain = LLMChain(llm=llm, prompt=PromptTemplate(template=prompt_template, input_variables=["context", "query"]))
    response = chain.run(context=context, query=query)
    return response
