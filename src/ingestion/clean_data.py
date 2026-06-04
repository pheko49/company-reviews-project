import pandas as pd
from pathlib import Path
#=====================
# Copied from notebook
#=====================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DATA_PATH = BASE_DIR / 'data' / 'raw' / 'company_data.csv'
PROCESSED_DATA_PATH = BASE_DIR / 'data' / 'processed' / 'cleaned_company_data.csv'
# read csv
# df = pd.read_csv('../data/raw/company_data.csv')
df = pd.read_csv(RAW_DATA_PATH)

# create copy of df
df1 = df.copy()

# remove missing values
df1 = df1.dropna(subset='Cities')

# remove duplicates
df1 = df1.drop_duplicates()
df1

# create conversion function
def convert_abbreviated_number(value):
    """
    Convert values  such as:
    72k Reviews -> 72000
    1.1L Reviews -> 110000
    96.1k Salaries ->  96100
    """

    value = str(value).strip()

    # Remove text labels
    value = value.replace(' Reviews', '')
    value = value.replace(' Salaries', '')
    # Handle missing values
    if value == '--':
        return None
    if value.endswith('k'):
        return float(value[:-1]) * 1_000
    elif value.endswith('L'):
        return float(value[:-1]) * 100_000
    else:
        return float(value)

# Create new numeric columns
df1['Reviews_Count'] = df1['Reviews'].apply(convert_abbreviated_number)
df1['Salary_Submissions'] = df1['Salaries'].apply(convert_abbreviated_number)

# remove missing values after creating new columns
df1 = df1.dropna(subset='Salary_Submissions')

# convert data types for new columns
df1['Reviews_Count'] = df1['Reviews_Count'].astype(int)
df1['Salary_Submissions'] = df1['Salary_Submissions'].astype(int)

# export to csv
df1.to_csv(
    PROCESSED_DATA_PATH,
    index=False
)

# print(PROCESSED_DATA_PATH)
# print(PROCESSED_DATA_PATH.parent.exists())