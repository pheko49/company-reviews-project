import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api import (
    get_companies,
    get_top_rated_companies,
    get_top_review_cities
)

def show_analytics():

    st.title('📈 Analytics Dashboard')

    top_rated = get_top_rated_companies()

    top_rated_df = pd.DataFrame(top_rated)

    fig = px.bar(
        top_rated_df,
        x='rating',
        y='company_name',
        orientation='h',
        title='Top Rated Companies'
    )

    st.plotly_chart(
        fig,
        # use_container_width=True
    )

    # Top Review Cities
    st.subheader('Top Review Cities')

    top_review_cities = get_top_review_cities()

    cities_df = pd.DataFrame(top_review_cities)

    fig = px.bar(
        cities_df,
        x='city',
        y='total_reviews',
        title='Top Review Cities'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Create scatter plot
    st.subheader('Relationship Between Ratings and Reviews')

    all_companies = get_companies()

    df = pd.DataFrame(data=all_companies)

    fig = px.scatter(
        df,
        x='reviews_count',
        y='rating',
        hover_name='company_name',
        title='Rating vs Reviews'
    )

    st.plotly_chart(fig)

