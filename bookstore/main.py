from fastapi import FastAPI

from bookstore.routers import books

app = FastAPI()
app.include_router(books.router)


@app.get('/', status_code=200, tags=['Welcome'])
async def welcome():
    """Welcome to my Bookstore"""
    return {'message': 'Welcome to my Bookstore'}
