from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from bookstore.database import get_session
from bookstore.models import Book
from bookstore.schemas import BookList, BookPublic, BookSchema

router = APIRouter(prefix='/books', tags=['Books'])


@router.get('/', response_model=BookList, status_code=HTTPStatus.OK)
async def list_books(session: Session = Depends(get_session)):
    """Lists all books"""
    books = session.scalars(select(Book))
    return {'books': books}


@router.get('/{book_id}', status_code=HTTPStatus.OK)
async def get_book(book_id: int, session: Session = Depends(get_session)):
    """Lists a book by ID"""
    book = session.scalar(select(Book).where(Book.book_id == book_id))
    if not book:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Book not found')
    return book


@router.post('/', status_code=HTTPStatus.CREATED, response_model=BookPublic)
async def add_book(book: BookSchema, session: Session = Depends(get_session)):
    """Insert a new book"""
    book_db = session.scalar(select(Book).where(Book.title == book.title))

    if book_db:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Book already exists',
        )

    book_db = Book(title=book.title)
    session.add(book_db)
    session.commit()
    session.refresh(book_db)

    return book_db


@router.delete('/{book_id}', status_code=HTTPStatus.OK)
async def delete_book(book_id: int, session: Session = Depends(get_session)):
    book_db = session.scalar(select(Book).where(Book.book_id == book_id))
    if not book_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Book not found')
    session.delete(book_db)
    session.commit()

    return {'message': 'Book deleted'}


@router.put('/{book_id}', response_model=BookPublic)
async def update_book(book_id: int, book: BookSchema, session: Session = Depends(get_session)):
    book_db = session.scalar(select(Book).where(Book.book_id == book_id))
    if not book_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Book not found")
    try:
        book_db.title = book.title
        session.commit()
        session.refresh(book_db)
        return book_db
    except IntegrityError:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Book already exists")
