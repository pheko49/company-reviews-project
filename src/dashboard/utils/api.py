import streamlit as st
import requests

BASE_URL = 'http://127.0.0.1:8000'

# Get all companies
@st.cache_data
def get_companies():
    response = requests.get(f'{BASE_URL}/companies')

    return response.json()

# Get top rated companies
@st.cache_data
def get_top_rated_companies():
    response = requests.get(
        f'{BASE_URL}/top-rated-companies'
    ).json()

    return response.json()

# Get top review cities
@st.cache_data
def get_top_review_cities():
     response = requests.get(
        f'{BASE_URL}/top-review-cities'
    )
     
     return response.json()

# Company search
@st.cache_data
def get_company(company_name):
    response = requests.get(
            f'{BASE_URL}/companies/{company_name}'
        )
    
    return response