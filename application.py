from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define the Book model with the specific parameters from your assignment
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} by {self.author}"

# Root route
@app.route('/')
def index():
    return 'Book API is running!'

# GET: Retrieve all books
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)
    return {"books": output}

# GET: Retrieve a single book by ID
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    }

# POST: Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    # Accepting the specific keys requested in the assignment
    book = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher']
    )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# DELETE: Delete a book by ID
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "book deleted"}