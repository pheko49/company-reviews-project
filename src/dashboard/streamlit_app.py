import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title='Company Reviews Dashboard',
    page_icon='📊',
    layout='wide'
)

API_URL = 'http://127.0.0.1:8000'

response = requests.get(f'{API_URL}/companies')

companies = response.json()

df = pd.DataFrame(data=companies)

st.title('📊 Company Reviews Dashboard')

st.dataframe(df)
