## [FastAPI: Build Python APIs in 1 Hour - Beginner](https://www.udemy.com/course/fastapi-construa-apis-em-python-em-1-hora-iniciante/)


## API Documentation

#### Returns all books

```http
  GET /books
```

#### Returns a book

```http
  GET /books/book_id
```

| Parameter   | Type       | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `book_id`   | `int`      | **Required**. The book's ID.                |

#### Inserts a new book

```http
  POST /books
```

| Parameter   | Type       | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `title  `   | `string`   | **Required**. The book's title.             |


#### Deletes a book

```http
  DELETE /books/book_id
```

| Parameter   | Type       | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `book_id`   | `int`      | **Required**. The book ID.                  |


#### Updates a book name

```http
  PUT /books/book_id
```

| Parameter   | Type       | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `book_id`   | `int`      | **Required**. The book ID.                  |
| `title  `   | `string`   | **Required**. The book's title.             |

---
## Running locally

Clone it:

```bash
  git clone https://github.com/wagnerhs-ciandt/FastAPI_in_1h
```

Change to its directory

```bash
  cd FastAPI_in_1h
```

Create a virtualenv

```bash
  python -m venv .venv
```

Activate the environment

```bash
  source .venv/bin/actiate
```

If `poetry` is not installed yet:
```bash
  pip install poetry
````

Install dependencies
```bash
  poetry install
```

Running the project
```bash
  fastapi dev bookstore/main.python
```

Running tests
```bash
  pytest