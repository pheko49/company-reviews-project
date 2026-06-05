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

    response = requests.get(
        'http://127.0.0.1:8000/top-review-cities'
    )

    cities_df = pd.DataFrame(
        response.json()
    )

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

    response = requests.get(
        'http://127.0.0.1:8000/companies'
    )

    df = pd.DataFrame(
        response.json()
    )

    fig = px.scatter(
        df,
        x='reviews_count',
        y='rating',
        hover_name='company_name',
        title='Rating vs Reviews'
    )

    st.plotly_chart(fig)

elif page == 'Company Search':

    st.title('🔍 Company Search')

    company_name = st.text_input(
        'Enter company name'
    )

    if company_name:

        response = requests.get(
            f'http://127.0.0.1:8000/companies/{company_name}'
        )

        if response.status_code == 200:

            company = response.json()

            st.write(company)
        else:
            st.error('Company not found')