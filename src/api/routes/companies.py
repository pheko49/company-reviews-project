from fastapi import APIRouter
# from sqlalchemy import text

# from src.database.connection import engine


from src.api.models import Company
from src.services.company_service import (
    get_company,
    get_top_rated_companies,
    get_most_reviewed_company,
    get_top_reviewed_city,
    get_companies_by_city
    )

router = APIRouter()

@router.get('/companies/{company_name}', response_model=Company)

def company(company_name: str):

    result = get_company(company_name)

    if result is None:
        return {'message': 'Company not found'}
    
    return result

@router.get('/top-rated-companies')
def top_rated_companies():

    return get_top_rated_companies()

@router.get('/most-reviewed-company')
def most_reviewed_company():

    return get_most_reviewed_company()

@router.get('/top-review-cities')
def top_review_cities():
    
    return get_top_reviewed_city()


@router.get('/companies-by-city/{city}')
def companies_by_city(city: str):

    return get_companies_by_city(city)


# @router.get('/companies/{comapny_name}')
# def get_company(company_name: str):

#     query = text("""
#         SELECT *
#         FROM company_reviews
#         WHERE company_name = :company_name
#     """)

    # with engine.connect() as conn:
    #     result = conn.execute(query)
        
    #     companies = [
    #         dict(row._mapping)
    #         for row in result
    #     ]
    
    # return companies

# @router.app('/companies')
# def get_companies():

#     query = text("""
#         SELECT *
#         FROM company_reviews
#         LIMIT 20
#     """)

#     with engine.connect() as conn:
#         result = conn.executive(query)

#         companies = [
#             dict(row._mapping)
#             for row in result
#         ]
    
#     return companies

