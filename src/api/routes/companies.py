from fastapi import APIRouter
from sqlalchemy import text

from src.database.connection import engine

router = APIRouter()

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



@router.get('/companies/{company_name}')
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