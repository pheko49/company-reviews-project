import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
from views.home import show_home
from views.analytics import show_analytics
from views.search import show_search

# page config
# st.set_page_config(
#     page_title='Company Reviews Dashboard',
#     page_icon='📊',
#     layout='wide'
# )

page = st.sidebar.selectbox(
    label='Navigation',
    options=[
        'Home',
        'Analytics',
        'Company Search'
    ]
)

if page == 'Home':
    show_home()

elif page == 'Analytics':
    show_analytics()

elif page == 'Company Search':
    show_search()
