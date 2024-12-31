from typing import List, Dict, Union

from fastapi import FastAPI


app = FastAPI()

FAKE_BOOKS_DATABASE: List[Dict[str, Union[int, str]]] = [
    {'id': 1, 'title': 'Learning Python: Powerful Object-Oriented Programming'},
    {'id': 2, 'title': 'Think Python: An Introduction to Software Design'},
    {'id': 3, 'title': 'Fluent Python: Clear, Concise, and Effective Programming'},
    {'id': 4, 'title': 'Web Scraping with Python: Collecting More Data from the Modern Web'},
    {'id': 5, 'title': 'Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners'},
    {'id': 6, 'title': 'Classic Computer Science Problems in Python'},
]


@app.get('/', status_code=200)
async def welcome():
    """Welcome to my Bookstore"""
    return {'message': 'Welcome to my Bookstore'}


@app.get('/books', status_code=200)
async def list_books():
    """Lists all books"""
    return {'books': FAKE_BOOKS_DATABASE}
