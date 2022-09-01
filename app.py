import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Excel Plotter")
st.title("Excel Plotter")
st.subheader("I'm hungry, feed me an Excel file!")

ExcelFile = st.file_uploader('What is on the menu?', type='xlsx')
if ExcelFile:
  st.markdown('---')
  df = pd.read_excel(ExcelFile, engine='openpyxl')
  st.dataframe

