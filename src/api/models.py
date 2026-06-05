from pydantic import BaseModel

class Company(BaseModel):
    company_id: int
    company_name: str
    rating: float
    company_type: str
    city: str
    reviews_count: int
    salary_submissions: int

class TopRatedCompany(BaseModel):
    company_name: str
    rating: float

class MostReviewedCompany(BaseModel):
    company_name: str
    reviews_count: int

class CityRating(BaseModel):
    city: str
    avg_rating: float