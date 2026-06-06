import streamlit as st

from utils.api import get_company

def show_search():
    st.title('🔍 Company Search')

    company_name = st.text_input(
        'Enter company name'
    )

    if company_name:

        response = get_company(company_name)

        if response.status_code == 200:

            company = response.json()

            st.write(company)

        elif response.status_code == 404:

            st.error('Company not found')

