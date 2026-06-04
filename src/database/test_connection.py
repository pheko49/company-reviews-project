from src.database.connection import engine
try:
    with engine.connect() as conn:
        print('Database connection successful!')
except Exception as e:
    print(f'Connection failed: {e}')