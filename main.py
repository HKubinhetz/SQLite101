from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    review = db.Column(db.Float, nullable=False)


# Create a new record
# new_book = Book(title="Harry Pottera", author="J. K. Rowling", review=9.3)
# db.session.add(new_book)
# db.session.commit()
#
# # Read All Books
# print(db.session.query(Book).all())
#
# # Read a Single Book
# print(Book.query.filter_by(title="Harry Potter").first())
#
# # Update a given entry:
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# # Delete a given entry:
# book_id = 3
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


# db.create_all()
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", review=9.3)
# db.session.add(new_book)
# db.session.commit()


