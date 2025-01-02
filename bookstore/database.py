from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from bookstore.settings import Settings

engine = create_engine(url=Settings().DATABASE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool)


def get_session():
    with Session(engine) as session:
        yield session
