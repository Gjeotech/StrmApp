import streamlit as st
import pandas as pd


st.write("""
    My First Chat App
""")


df = pd.read_csv('C:/Users/brand/Desktop/n8nproject/Cupcakes.csv')
st.line_chart(df)



