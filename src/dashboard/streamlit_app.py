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

total_companies = len(df)

average_rating = round(df['rating'].mean(), 2)

total_reviews = df['reviews_count'].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label='Total Companies',
        value=total_companies
    )

with col2:
    st.metric(
        label='Average Rating',
       value=average_rating
    )

with col3:
    st.metric(
        label='Total Reviews',
        value=f'{total_reviews:,}'
    )

st.dataframe(df)