# Streamlit Web Application Interface
import streamlit as st
import pandas as pd
import numpy as np

st.title("🛍️ AI Product Recommendation System")
st.write("USC AI Capstone - Intelligent Product Discovery")

# Sidebar for user input
st.sidebar.header("Tell us what you're looking for")
user_query = st.sidebar.text_input("What product are you interested in?", "running shoes")
budget = st.sidebar.slider("Budget range", 0, 1000, 200)

if st.sidebar.button("Get Recommendations"):
    st.write(f"### Recommendations for: {user_query}")
    st.write(f"Budget: ${budget}")
    
    # Mock recommendations
    recommendations = [
        {"Product": "Nike Air Max", "Price": "$150", "Match": "95%"},
        {"Product": "Adidas Ultraboost", "Price": "$180", "Match": "92%"},
        {"Product": "New Balance 990", "Price": "$175", "Match": "88%"}
    ]
    
    df = pd.DataFrame(recommendations)
    st.dataframe(df)
    
    st.write("### AI Explanation")
    st.write(f"Based on your search for '{user_query}' and budget of ${budget}, I analyzed product features, user reviews, and price points to find the best matches.")

st.write("---")
st.write("*Demo version - Full system uses GPT-4, collaborative filtering, and real product databases*")
