from fastapi import FastAPI

from src.api.routes import router
app = FastAPI()

@app.get('/')
def home():
    return {
        'message': 'Company Reviews API 🚀'
    }

app.include_router(router)