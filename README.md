

# FastAPI Project for Blogs Website

This project is a REST API for a blogs website, developed using FastAPI. It incorporates modern development practices and tools to ensure robust and efficient performance.

## Key Features

### Environment
- **Poetry**: Manages dependencies and virtual environments.

### Database
- **ORM with SQLAlchemy**: Provides seamless interaction with the database.

### API Development
- **FastAPI**: Powers the REST API endpoints.
- **Status Codes and HTTPExceptions**: Handles responses and errors.
- **Repository Design Pattern**: Abstracts data access logic for separation of concerns.
- **Routes**: Organizes API routes for various functionalities.

### Authentication
- **JWT**: Implements JSON Web Tokens for secure authentication.
- **OAuth2**: Integrates OAuth2 for enhanced authentication and third-party service support.

### Async Operations
- **Async I/O**: Utilizes asynchronous programming for improved performance.

### Containerization
- **Docker**: Containers the application for consistent environments across development and production.

### Testing
- **Pytest**: Writes and executes tests.
- **Mock DB**: Uses a mock database for initial test cases.

## Updates (As of 11/8)
1. **Database Engine**: Transitioned from SQLite to PostgreSQL to leverage advanced features and improve performance.
2. **Database mangement Tool**: Integrated adminpg for managing and viewing the PostgreSQL database.


## To-Do List
1. ** sturtce projetc**
2. **Database Migration Tool**: Continue using Alembic for migrations.
3. **Separate Databases**: Maintain and manage separate databases for production and testing.
4. **Comprehensive Unit Tests**: Develop unit tests using the test database.

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/MohanadGad38/Blog-with-jwt-unit-testing.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Blog-with-jwt-unit-testing
   ```
3. **Install dependencies:**
   ```bash
   poetry install
   ```
4. **Set up the databases:**
   - Ensure PostgreSQL is running.
   - Create the `blog`  databases:
     ```sql
     CREATE DATABASE blog;
     ```
   - Configure database URLs in your `.env` file.


6. **Run the application:**
   ```bash
   docker-compose up
   ```

## Usage
Visit `http://localhost:8000` to access the API.

## Contributing
To contribute, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. 

---
