from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'postgresql://bookuser:bookpass@localhost:5432/bookdb'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date.isoformat()
        }

# Create tables
with app.app_context():
    db.create_all()

# Helper function for error responses
def error_response(message, status_code):
    return jsonify({'error': message}), status_code

# Helper function for validation
def validate_book_data(data):
    required_fields = ['title', 'author', 'published_date']
    for field in required_fields:
        if field not in data or not data[field]:
            return f"Missing required field: {field}"
    
    # Validate date format
    try:
        datetime.strptime(data['published_date'], '%Y-%m-%d')
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD"
    
    return None

# Routes
@app.route('/books', methods=['GET'])
def get_books():
    """Get all books"""
    try:
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])
    except Exception as e:
        return error_response(f"Error retrieving books: {str(e)}", 500)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Get a specific book by ID"""
    try:
        book = Book.query.get(book_id)
        if not book:
            return error_response("Book not found", 404)
        return jsonify(book.to_dict())
    except Exception as e:
        return error_response(f"Error retrieving book: {str(e)}", 500)

@app.route('/books', methods=['POST'])
def create_book():
    """Create a new book"""
    try:
        data = request.get_json()
        if not data:
            return error_response("No JSON data provided", 400)
        
        # Validate input
        validation_error = validate_book_data(data)
        if validation_error:
            return error_response(validation_error, 400)
        
        # Create new book
        book = Book(
            title=data['title'],
            author=data['author'],
            published_date=datetime.strptime(data['published_date'], '%Y-%m-%d').date()
        )
        
        db.session.add(book)
        db.session.commit()
        
        return jsonify(book.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return error_response(f"Error creating book: {str(e)}", 500)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """Update an existing book"""
    try:
        book = Book.query.get(book_id)
        if not book:
            return error_response("Book not found", 404)
        
        data = request.get_json()
        if not data:
            return error_response("No JSON data provided", 400)
        
        # Validate input
        validation_error = validate_book_data(data)
        if validation_error:
            return error_response(validation_error, 400)
        
        # Update book
        book.title = data['title']
        book.author = data['author']
        book.published_date = datetime.strptime(data['published_date'], '%Y-%m-%d').date()
        
        db.session.commit()
        
        return jsonify(book.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return error_response(f"Error updating book: {str(e)}", 500)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Delete a book"""
    try:
        book = Book.query.get(book_id)
        if not book:
            return error_response("Book not found", 404)
        
        db.session.delete(book)
        db.session.commit()
        
        return jsonify({'message': 'Book deleted successfully'}), 200
    
    except Exception as e:
        db.session.rollback()
        return error_response(f"Error deleting book: {str(e)}", 500)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)