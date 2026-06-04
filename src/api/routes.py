from fastapi import APIRouter
from sqlalchemy import text

from src.database.connection import engine

router = APIRouter()

@router.get('/companies')
def get_companies():

    query = text("""
        SELECT *
        FROM company_reviews
        LIMIT 20
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        
        companies = [
            dict(row._mapping)
            for row in result
        ]
    
    return companies