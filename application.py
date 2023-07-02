from flask import Flask
app = Flask(__name__)

class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(20), nullable=False)
    publisher = Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def index():
    books = Book.query.all()
    return {"books": books}