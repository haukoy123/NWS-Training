from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime



engine = create_engine("mysql://root:hau1999@localhost:5432/db_test_driven",echo = True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()



class Book_Author(Base):
    __tablename__ = 'book_author'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id', ondelete="CASCADE"))
    book_id = Column(Integer, ForeignKey('book.id', ondelete="CASCADE"))

 


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date_birth = Column(DateTime())
    book = relationship("Book", secondary=Book_Author.__tablename__, backref='authors', passive_deletes=True, cascade="all, delete")
    def __repr__(self):
        return "<Author(%s)>" %self.name 


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    author = relationship("Author", secondary=Book_Author.__tablename__, backref='books', passive_deletes=True, cascade="all, delete")
    def __repr__(self):
        return "<Book(%s)>" %self.name 

Base.metadata.create_all(engine)

