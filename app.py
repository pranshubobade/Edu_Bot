import streamlit as st
from transformers import pipeline

# Load Hugging Face QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# App title
st.title("Educational Q&A Bot")
st.write("Ask me questions about different topics!")

# Topic selection
topic = st.selectbox("Choose a topic:", ["General Education", "Math", "Science"])

# Contexts for each topic
if topic == "General Education":
    context = """Education is the process of acquiring knowledge, skills, values, and attitudes.
It can occur in formal settings like schools or informally through life experiences.
Modern education aims to foster critical thinking, prepare people for jobs, and promote lifelong learning.
Tools like online courses, AI tutors, and collaboration platforms are increasingly used."""
    
elif topic == "Math":
    context = """Mathematics is the study of numbers, shapes, quantities, and patterns.
It includes fields like arithmetic, algebra, geometry, and calculus.
Math is essential in science, engineering, finance, and everyday problem-solving.
Concepts like equations, graphs, and functions are key to understanding the world mathematically."""
    
elif topic == "Science":
    context = """Science is the study of the natural world through observation and experiment.
It includes fields like physics, chemistry, biology, and earth science.
Scientists use the scientific method to ask questions, collect data, and form conclusions.
Science helps us understand how things work and improve technologies that affect our lives."""

# User question input
question = st.text_input("Ask your question:")

# Answer the question
if question:
    result = qa_pipeline(question=question, context=context)
    st.write(f"**Answer:** {result['answer']}")
