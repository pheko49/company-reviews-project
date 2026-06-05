from sqlalchemy import text

from src.database.connection import engine

def get_all_companies():

    query = text("""
        SELECT
            company_id,
            company_name,
            rating,
            company_type,
            city,
            reviews_count,
            salary_submissions
        FROM company_reviews   
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        companies = [
            dict(row._mapping)
            for row in result
        ]
    
    return companies

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
        # return {'message': 'Companny not found'}
        return None
    
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

def get_top_reviewed_city():

    query = text("""
                 SELECT
                    city,
                    SUM(reviews_count) AS total_reviews
                 FROM company_reviews
                 GROUP BY city
                 ORDER BY total_reviews DESC
                 LIMIT 10

                 """)
    
    with engine.connect() as conn:

        result = conn.execute(query)

        cities = [
            dict(row._mapping)
            for row in result
        ]
    
    return cities

def get_companies_by_city(city: str):

    query = text("""
        SELECT
            company_name,
            rating,
            company_type,
            city
        FROM company_reviews
        WHERE city = :city
        ORDER BY rating DESC    
    """)

    with engine.connect() as conn:

        result = conn.execute(
            query,
            {'city': city}
        )

        companies = [
            dict(row._mapping)
            for row in result
        ]

    return companies

def get_companies_by_rating(min_rating: float):
    
    query = text("""
        SELECT
            company_name,
            rating,
            city
        FROM company_reviews
        WHERE rating >= :min_rating
        ORDER BY rating DESC
        """)
    
    with engine.connect() as conn:

        result = conn.execute(
            query,
            {'min_rating': min_rating}
        )
        companies = [
            dict(row._mapping)
            for row in result
        ]

    return companies