import streamlit as st
import requests
import pandas as pd
import plotly.express as px

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
if page == 'Home':
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

elif page == 'Analytics':

    st.title('📈 Analytics Dashboard')

    top_rated = requests.get(
        f'{API_URL}/top-rated-companies'
    ).json()

    top_rated_df = pd.DataFrame(top_rated)

    fig = px.bar(
        top_rated_df,
        x='company_name',
        y='rating',
        title='Top Rated Companies'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )