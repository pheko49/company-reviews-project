from pathlib import Path

import pandas as pd

from src.database.connection import engine

BASE_DIR = Path(__file__).resolve().parents[2]

file_path = (
    BASE_DIR
    / 'data'
    / 'processed'
    / 'cleaned_company_data.csv'
)

df = pd.read_csv(file_path)

# Rename columns to match PostgreSQL schema
df = df.rename(
    columns={
        'Name': 'company_name',
        'Rating': 'rating',
        'Company_type': 'company_type',
        'Cities': 'city',
        'Reviews_Count': 'reviews_count',
        'Salary_Submissions': 'salary_submissions'
    }
)

# Keep only columns needed in database
df = df[
    [
        'company_name',
        'rating',
        'company_type',
        'city',
        'reviews_count',
        'salary_submissions'

    ]
]

df.to_sql(
    name='company_reviews',
    con=engine,
    if_exists='append',
    index=False
)

print(f'{len(df)} rows loaded successfully.')