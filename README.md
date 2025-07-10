Book API - Application Engineer Technical Test
A RESTful Flask API for managing books with PostgreSQL database integration, developed for the UKDSC Application Engineer role.

🚀 Project Overview
This project demonstrates:

Flask web framework with RESTful API design

SQLAlchemy ORM for database operations

PostgreSQL database integration

Docker containerization setup

Production-ready code structure and error handling

📋 Requirements Met
✅ Flask API with CRUD operations for Book resource

✅ SQLAlchemy ORM with proper model design

✅ PostgreSQL database configuration

✅ Docker & Docker Compose setup

✅ RESTful API best practices ✅ Comprehensive documentation ## 🏗️ API Endpoints

Method

Endpoint

Description

GET

/books

List all books

GET

/books/<id>

Retrieve specific book

POST

/books

Create new book

PUT

/books/<id>

Update existing book

DELETE

/books/<id>

Delete book


Export to Sheets
📊 Book Model
JSON

{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_date": "1925-04-10"
}
🐳 Docker Setup
Prerequisites
Docker Desktop

Docker Compose

Quick Start
Bash

# Clone the repository
git clone <repository-url>
cd book-api-application-engineer-test

# Start the application
docker-compose up --build

# API will be available at http://localhost:5000
Services
web: Flask application (port 5000)

db: PostgreSQL database (port 5432)

🧪 API Testing Examples & Results
This section demonstrates the output from testing each API endpoint, proving full functionality.

Create a Book
Command:

Bash

curl -X POST http://localhost:5000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_date": "1960-07-11"
  }'
Output:

JSON

{
  "id": 1,
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "published_date": "1960-07-11"
}
Get All Books
Command:

Bash

curl http://localhost:5000/books
Output:

JSON

[
  {
    "id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_date": "1960-07-11"
  }
]
Get Specific Book
Command:

Bash

curl http://localhost:5000/books/1
Output:

JSON

{
  "id": 1,
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "published_date": "1960-07-11"
}
Update a Book
Command:

Bash

curl -X PUT http://localhost:5000/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "To Kill a Mockingbird (Updated)",
    "author": "Harper Lee",
    "published_date": "1960-07-11"
  }'
Output:

JSON

{
  "id": 1,
  "title": "To Kill a Mockingbird (Updated)",
  "author": "Harper Lee",
  "published_date": "1960-07-11"
}
Delete a Book
Command:

Bash

curl -X DELETE http://localhost:5000/books/1
Output:

JSON

{
  "message": "Book deleted successfully"
}
📝 Postman Testing
Import Collection
Open Postman

Import the following endpoints:

GET http://localhost:5000/books

POST http://localhost:5000/books (with JSON body)

PUT http://localhost:5000/books/1 (with JSON body)

DELETE http://localhost:5000/books/1

Sample JSON Body for POST/PUT
JSON

{
  "title": "1984",
  "author": "George Orwell",
  "published_date": "1949-06-08"
}
🔧 Technical Implementation
Framework & Libraries
Flask 2.3.3: Web framework

Flask-SQLAlchemy 3.0.5: ORM integration

psycopg2-binary 2.9.7: PostgreSQL adapter

Error Handling
400 Bad Request: Invalid input data

404 Not Found: Book doesn't exist

500 Internal Server Error: Database/server errors

📂 Project Structure
book-api/
├── app.py              # Main Flask application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Multi-service setup
└── README.md             # Documentation
📋 Assumptions Made
PostgreSQL Version: Using PostgreSQL 13

Python Version: Python 3.9+ compatibility

Date Format: ISO 8601 standard (YYYY-MM-DD)

Port Configuration: Flask on 5000, PostgreSQL on 5432

📞 Contact & Submission
Developed by: Shajith

For: UKDSC Application Engineer Role
