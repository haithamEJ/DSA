import streamlit as st
import pandas as pd

# Set the title of the app
st.title('Excel File Uploader')

# Allow users to upload an Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

# If a file is uploaded, read and display the data
if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    
    # Display the data inside the file
    st.write(df)
