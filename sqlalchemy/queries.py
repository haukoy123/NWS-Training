from sqlalchemy.sql.expression import desc
from models import Author, Book, Book_Author, Session


session = Session()
# insert data

# author_1 = Author(name="hau")
# author_2 = Author(name="minh")
# author_3 = Author(name="lam")
# book_1 = Book(name="van 2")
# book_2 = Book(name="van")
# book_3 = Book(name="toan 2")

# author_2.book.extend([book_1, book_2])
# session.add(author_2)
# book_1.author.append(author_1)
# session.add(book_1)
# author_3.book.append(book_3)
# session.add(author_3)
# session.commit()



# delete data
from sqlalchemy import func
# # authors = session.query(Author.name.label('author_name'), Book.name.label('book_name')).select_from(Author).join(Book_Author).join(Book).filter(Author.name=='hau').all()
# # count_author = session.query(func.count(Author.name).label('count')).first()
# authors = session.query(Author).filter(Author.name=='minh')
authors = session.query(
        func.count(Book.name).label('count')
    ).select_from(Author).join(Book_Author).join(Book).filter(Author.name=='minh').first()

print(authors.count)
# # # print(count_author.keys())
# # # print(count_author.count)
# # print(authors[0].book_name)
# authors.delete()
# session.commit()
