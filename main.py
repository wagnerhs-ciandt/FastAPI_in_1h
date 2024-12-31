from random import choice
from typing import List, Dict, Union
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from schemas import Book, BookPublic


app = FastAPI()

FAKE_BOOKS_DATABASE: List[Dict[str, Union[int, str]]] = [
    {'book_id': uuid4().hex, 'title': 'Learning Python: Powerful Object-Oriented Programming'},
    {'book_id': uuid4().hex, 'title': 'Think Python: An Introduction to Software Design'},
    {'book_id': uuid4().hex, 'title': 'Fluent Python: Clear, Concise, and Effective Programming'},
    {'book_id': uuid4().hex, 'title': 'Web Scraping with Python: Collecting More Data from the Modern Web'},
    {
        'book_id': uuid4().hex,
        'title': 'Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners',
    },
    {'book_id': uuid4().hex, 'title': 'Classic Computer Science Problems in Python'},
]


@app.get('/', status_code=200)
async def welcome():
    """Welcome to my Bookstore"""
    return {'message': 'Welcome to my Bookstore'}


@app.get('/books', status_code=200)
async def list_books():
    """Lists all books"""
    return {'books': FAKE_BOOKS_DATABASE}


@app.get('/books/{book_id}', status_code=200)
async def get_book(book_id: int):
    """Lists a book by ID"""
    if book_id <= 0:
        raise HTTPException(status_code=400, detail='book_id must be greater than 0')
    try:
        book = FAKE_BOOKS_DATABASE[book_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail='Book not found')
    return {'book': book}


@app.post('/books', status_code=201, response_model=BookPublic)
async def add_book(book: Book):
    """Insert a new book"""
    if not book.title.strip():
        raise HTTPException(status_code=400, detail='Need to add a valid name')

    book_id = uuid4().hex
    new_book = BookPublic(book_id=book_id, title=book.title)
    json_book = jsonable_encoder(new_book)

    if any([book.title == books['title'] for books in FAKE_BOOKS_DATABASE]):
        raise HTTPException(status_code=400, detail='Book already exists')

    FAKE_BOOKS_DATABASE.append(json_book)
    return {'title': book.title}
