from pydantic import BaseModel

class Company(BaseModel):
    company_id: int
    company_name: str
    rating: float
    company_type: str
    city: str
    reviews_count: int
    salary_submissions: int
