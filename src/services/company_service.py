from sqlalchemy import text

from src.database.connection import engine


def get_company(company_name: str):
    
    query = text("""
        SELECT *
        FROM company_reviews
        WHERE company_name = :company_name
    """)
    
    with engine.connect() as conn:

        result = conn.execute(
            query,
            {'company_name': company_name}
        )

        company = result.fetchone()

    if company is None:
        return {'message': 'Companny not found'}
    
    return dict(company._mapping)

def get_top_rated_companies():

    query = text("""
        SELECT
            company_name,
            rating
        FROM company_reviews
        ORDER BY rating DESC
        LIMIT 10 
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        companies = [
            dict(row._mapping)
            for row in result
        ]

    return companies

def get_most_reviewed_company():

    query = text("""
        SELECT
            company_name,
            reviews_count
        FROM company_reviews
        ORDER BY reviews_count DESC
        LIMIT 10
    """)

    with engine.connect() as conn:
        
        result = conn.execute(query)

        companies = [
            dict(row._mapping)
            for row in result
        ]
    
    return companies