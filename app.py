import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Excel Plotter")
st.title("Excel Plotter")
st.subheader("I'm hungry, feed me an Excel file!")

upload_file = st.file_uploader('What is on the menu?', type='xlsx')
if uploaded_file:
  st.markdown('---')
  df = pd.read_excel(uploaded_file, engine='openpyxl')
  st.dataframe

