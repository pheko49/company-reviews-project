CREATE TABLE company_reviews (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    rating DECIMAL(2,1),
    company_type VARCHAR(255),
    city VARCHAR(255),
    reviews_count INTEGER,
    salary_submissions INTEGER
);