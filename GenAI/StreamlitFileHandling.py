"""
StreamlitFileHandling.py

This script is to save the file uploaded through streamlit app to the local directory for later processing.

Author: Subin
Date: April 16, 2025
"""
# Importing the required libraries
import streamlit as st
import os

# Function to save uploaded file to specified directory
def save_uploaded_file(uploaded_file, save_dir=r"C:\Users\subin\OneDrive\Desktop\GenAI\Input"):
    if uploaded_file is None:
        return None
    # Ensure the directory exits
    os.makedirs(save_dir,exist_ok=True)

    # Define the file path
    file_path = os.path.join(save_dir,uploaded_file.name)

    # Write the uploaded file to the specified path
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    print(file_path)
    return file_path

