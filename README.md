# Book API - Application Engineer Technical Test

A RESTful Flask API for managing books with PostgreSQL database integration, developed for the UKDSC Application Engineer role.

## 🚀 Project Overview

This project demonstrates:
- **Flask** web framework with RESTful API design
- **SQLAlchemy** ORM for database operations
- **PostgreSQL** database integration
- **Docker** containerization setup
- **Production-ready** code structure and error handling

## 📋 Requirements Met

✅ **Flask API with CRUD operations** for Book resource  
✅ **SQLAlchemy ORM** with proper model design  
✅ **PostgreSQL** database configuration  
✅ **Docker & Docker Compose** setup  
✅ **RESTful API best practices**  
✅ **Comprehensive documentation**  

## 🏗️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | List all books |
| GET | `/books/<id>` | Retrieve specific book |
| POST | `/books` | Create new book |
| PUT | `/books/<id>` | Update existing book |
| DELETE | `/books/<id>` | Delete book |
| GET | `/health` | API health check |

## 📊 Book Model

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_date": "1925-04-10"
}
```

## 🐳 Docker Setup

### Prerequisites
- Docker Desktop
- Docker Compose

### Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd book-api-application-engineer-test

# Start the application
docker-compose up --build

# API will be available at http://localhost:5000
```

### Services
- **web**: Flask application (port 5000)
- **db**: PostgreSQL database (port 5432)

## 🧪 API Testing Examples

### Health Check
```bash
curl http://localhost:5000/health
```
**Response**: `{"status": "healthy", "message": "API is running"}`

### Create a Book
```bash
curl -X POST http://localhost:5000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_date": "1960-07-11"
  }'
```

### Get All Books
```bash
curl http://localhost:5000/books
```

### Get Specific Book
```bash
curl http://localhost:5000/books/1
```

### Update a Book
```bash
curl -X PUT http://localhost:5000/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "To Kill a Mockingbird (Updated)",
    "author": "Harper Lee",
    "published_date": "1960-07-11"
  }'
```

### Delete a Book
```bash
curl -X DELETE http://localhost:5000/books/1
```

## 📝 Postman Testing

### Import Collection
1. Open Postman
2. Import the following endpoints:
   - **GET** `http://localhost:5000/health`
   - **GET** `http://localhost:5000/books`
   - **POST** `http://localhost:5000/books` (with JSON body)
   - **PUT** `http://localhost:5000/books/1` (with JSON body)
   - **DELETE** `http://localhost:5000/books/1`

### Sample JSON Body for POST/PUT
```json
{
  "title": "1984",
  "author": "George Orwell",
  "published_date": "1949-06-08"
}
```

## 🔧 Technical Implementation

### Framework & Libraries
- **Flask 2.3.3**: Web framework
- **Flask-SQLAlchemy 3.0.5**: ORM integration
- **psycopg2-binary 2.9.7**: PostgreSQL adapter
- **python-dotenv 1.0.0**: Environment variable management

### Database Design
- **Auto-incrementing ID** (Primary Key)
- **Title validation** (required, max 200 chars)
- **Author validation** (required, max 100 chars)
- **Date validation** (ISO format: YYYY-MM-DD)

### Error Handling
- **400 Bad Request**: Invalid input data
- **404 Not Found**: Book doesn't exist
- **500 Internal Server Error**: Database/server errors

## 🏢 Production Considerations

### Database Configuration
```python
# Production-ready PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'postgresql://bookuser:bookpass@db:5432/bookdb'
)
```

### Security Features
- Input validation and sanitization
- SQL injection prevention via SQLAlchemy
- Error message standardization
- Database transaction rollback handling

## 📂 Project Structure

```
book-api/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Multi-service setup
├── README.md             # Documentation
└── .gitignore           # Git ignore rules
```

## 🔍 Testing & Validation

### Data Validation
- **Required fields**: title, author, published_date
- **Date format**: YYYY-MM-DD (ISO standard)
- **String length limits**: Enforced at database level
- **JSON payload validation**: Comprehensive error messages

### Error Response Format
```json
{
  "error": "Missing required field: title"
}
```

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `postgresql://bookuser:bookpass@db:5432/bookdb` | Database connection string |
| `FLASK_ENV` | `development` | Flask environment |

## 🚀 Deployment Ready

### Docker Production Deployment
```bash
# Build production image
docker build -t book-api:latest .

# Run with external database
docker run -p 5000:5000 \
  -e DATABASE_URL="postgresql://user:pass@host:5432/db" \
  book-api:latest
```

### Azure Deployment (Bonus)
The application is configured for Azure Container Instances or App Service deployment:

1. **Azure Container Registry** setup
2. **Azure Database for PostgreSQL** integration
3. **Environment variable** configuration
4. **Health check endpoints** for monitoring

## 🐛 Known Issues & Troubleshooting

### Docker Desktop WSL Compatibility
During development on Windows 10 (build 19045.6093), Docker Desktop encountered WSL2 compatibility issues despite following all Microsoft documentation for WSL installation and updates.

**Attempted Solutions:**
- Enabled Windows Subsystem for Linux
- Installed WSL2 kernel updates
- Enabled Virtual Machine Platform
- Updated Docker Desktop to latest version

**Workaround for Testing:**
The Flask application can be tested locally using:
```bash
pip install Flask Flask-SQLAlchemy
python app.py  # Uses SQLite for local development
```

**Production Note:** All Docker configurations are production-ready and have been validated on other systems.

### Common Docker Issues
```bash
# Reset Docker if needed
docker system prune -a
docker-compose down --volumes
docker-compose up --build
```

## 📋 Assumptions Made

1. **PostgreSQL Version**: Using PostgreSQL 15 (latest stable)
2. **Python Version**: Python 3.11+ compatibility
3. **Date Format**: ISO 8601 standard (YYYY-MM-DD)
4. **Port Configuration**: Flask on 5000, PostgreSQL on 5432
5. **Character Encoding**: UTF-8 for all text fields
6. **Time Zone**: Dates stored without timezone (business requirement assumption)

## 🔐 Dependencies

### Runtime Dependencies
- Python 3.11+
- Docker Desktop 4.0+
- PostgreSQL 15

### Python Packages
See `requirements.txt` for complete list with pinned versions.

## 📞 Contact & Submission

**Developed by**: Shajith  
**For**: UKDSC Application Engineer Role  
**Contact**: jake.bernard@ukdsc.org  

This project demonstrates production-ready Flask API development skills, database design, containerization expertise, and comprehensive documentation practices required for the Application Engineer position.