import streamlit as st
import requests
import pandas as pd

# page config
st.set_page_config(
    page_title='Company Reviews Dashboard',
    page_icon='📊',
    layout='wide'
)

# api call
API_URL = 'http://127.0.0.1:8000'

response = requests.get(f'{API_URL}/companies')

companies = response.json()

# dataframe
df = pd.DataFrame(data=companies)

# sidebar
page = st.sidebar.selectbox(
    label='Navigation',
    options=[
        'Home', 'Analytics', 'Company Search'
    ]
)

# title
st.title('📊 Company Reviews Dashboard')

#kpis
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

# table/dataframe
st.dataframe(df)