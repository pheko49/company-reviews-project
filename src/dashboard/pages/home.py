import streamlit as st
import pandas as pd

from utils.api import get_companies

def show_home():

    companies = get_companies()

    df = pd.DataFrame(data=companies)

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

