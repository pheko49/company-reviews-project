import streamlit as st
import requests
import os

# BASE_URL = 'http://127.0.0.1:8000'

# BASE_URL = 'http://host.docker.internal:8000'

BASE_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

# Get all companies
# @st.cache_data
# def get_companies():
#     response = requests.get(f'{BASE_URL}/companies')

#     response.raise_for_status()

#     return response.json()
@st.cache_data
def get_companies():
    try:
        response = requests.get(
            f'{BASE_URL}/companies',
            timeout=30
        )

        response.raise_for_status()

        return response.json()
    
    except requests.exceptions.RequestException:
        st.warning(
            'The API is still waking up. Please wait a few seconds and refresh the page.'
        )
        return []


# Get top rated companies
@st.cache_data
def get_top_rated_companies():
    response = requests.get(
        f'{BASE_URL}/top-rated-companies'
    )

    return response.json()

# Get top review cities
@st.cache_data
def get_top_review_cities():
     response = requests.get(
        f'{BASE_URL}/top-review-cities'
    )
     
     response.raise_for_status()

     return response.json()

# Company search
@st.cache_data
def get_company(company_name):
    response = requests.get(
            f'{BASE_URL}/companies/{company_name}'
        )

    return response