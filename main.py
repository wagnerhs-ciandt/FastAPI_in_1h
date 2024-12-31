from typing import List, Dict, Union

from fastapi import FastAPI, HTTPException


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


@app.get('/books/{bookd_id}', status_code=200)
async def get_book(book_id: int):
    """Lists a book by ID"""
    if book_id <= 0:
        raise HTTPException(status_code=400, detail='book_id must be greater than 0')
    try:
        book = FAKE_BOOKS_DATABASE[book_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail='Book not found')
    return {'book': book}


@app.post('/books', status_code=201)
async def add_book(name: str):
    """Insert a new book"""
    print('NAME: ', name)
    if not name.strip():
        return {'error': 'Need to add a valid name'}
    if any([name == book['title'] for book in FAKE_BOOKS_DATABASE]):
        return {'message': 'Book already exists'}
    if FAKE_BOOKS_DATABASE:
        highest_id = max(FAKE_BOOKS_DATABASE, key=lambda book: book['id']).get('id')
        FAKE_BOOKS_DATABASE.append({'id': highest_id + 1, 'title': name})
        return {'message': 'New book added'}
    return {'message': 'No books available'}
