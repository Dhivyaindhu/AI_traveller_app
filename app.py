# -*- coding: utf-8 -*-
"""Untitled143.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vsyUGX1MQjloFU7iw97HBFJq-PnpuF-v
"""

import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Set up Streamlit app title
st.title("AI Travel Cost Estimator")

# Use environment variable for API Key (Ensure it's set before running)
gemini_API_KEY = os.getenv("GEMINI_API_KEY")  # Correct way to access API key

# Validate API key
if not gemini_API_KEY or gemini_API_KEY =="AIzaSyCBxouxQ_5gN9ikG_RK9a6WNUotzglMVmE":
    st.error("Please set your Gemini API key as an environment variable.")
else:
    # Define the prompt template
    chat_template = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant who estimates travel costs for different modes of transport from {source} to {destination}. You provide cost breakdowns and recommendations for major places."),
        ("human", "Book a flight, train, bus, or car travel from {source} to {destination}.")
    ])

    # Initialize the chat model
    chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemini_API_KEY)

    # Define the processing pipeline
    parser = StrOutputParser()

    # Streamlit UI Inputs
    source = st.text_input("Enter Source Location:")
    destination = st.text_input("Enter Destination Location:")

    if st.button("Estimate Cost"):
        if source and destination:
            try:
                # Format prompt properly
                formatted_prompt = chat_template.format_messages(source=source, destination=destination)

                # Invoke the model with user input
                response = chat_model.invoke(formatted_prompt)

                # Parse and display the response
                parsed_response = parser.parse(response)
                st.write(parsed_response)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter both source and destination.")