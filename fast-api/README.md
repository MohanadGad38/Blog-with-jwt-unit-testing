
# FastAPI Project for Blogs Website

This project is a REST API for a blogs website, developed using FastAPI. It incorporates modern development practices and tools to ensure robust and efficient performance.

## Key Features

### Environment
- **Poetry**: Manages dependencies and virtual environments.

### Database
- **SQLAlchemy ORM**: Provides seamless interaction with the database.

### API Development
- **FastAPI**: Powers the REST API endpoints.
- **Status Codes and HTTPExceptions**: Manages responses and errors.
- **Repository Design Pattern**: Abstracts data access logic for better separation of concerns.
- **Routes**: Organizes API routes for various functionalities.

### Authentication
- **JWT**: Implements JSON Web Tokens for secure authentication.
- **OAuth2**: Integrates OAuth2 for enhanced authentication and third-party service support.

### Async Operations
- **Async I/O**: Utilizes asynchronous programming for improved performance.

### Containerization
- **Docker**: Containers the application for consistent environments across development and production.

### Testing
- **Pytest**: Facilitates writing and executing tests.
- **Mock DB**: Uses a mock database for initial test cases.

## Recent Updates (As of 11/8)
1. **Database Engine**: Transitioned from SQLite to PostgreSQL for advanced features and improved performance.
2. **Database Management Tool**: Integrated `adminpg` for managing and viewing the PostgreSQL database.

## To-Do List
1. **Structure the project**
2. **Database Migration Tool**: Continue using Alembic for migrations.
3. **Separate Databases**: Maintain and manage separate databases for production and testing environments.
4. **Comprehensive Unit Tests**: Develop more unit tests using the test database.

## Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MohanadGad38/Blog-with-jwt-unit-testing.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Blog-with-jwt-unit-testing
   ```

3. **Create environment files:**

   In the `fast-api` folder, you need to create two environment files:

   - **`database_mangement.env`**
     ```bash
     PGADMIN_DEFAULT_EMAIL="test@gmail.com"
     PGADMIN_DEFAULT_PASSWORD="test"
     ```

   - **`database.env`**
     ```bash
     POSTGRES_USER="MM"
     POSTGRES_PASSWORD="1G"
     POSTGRES_DB=Blog
     ```

4. **Set up the databases:**
   - Ensure PostgreSQL is running.
   - Create the `blog` database:
     ```sql
     CREATE DATABASE blog;
     ```
   - Configure the database URL in your `.env` file.

5. **Run the application using Docker:**
   ```bash
   docker-compose up
   ```

6. **Alternatively, run the application without Docker:**
   - Ensure PostgreSQL is running.
   - Install dependencies:
     ```bash
     poetry install
     ```
   - Start the application using your local environment setup.

## Environment Configuration

Ensure that you add the `.env` file inside the `fast-api` folder with the following content, adjusting the values as necessary for your setup:

```bash
DATABASE_URL="postgresql+asyncpg://MM:1G@localhost:5432/blog"
```

Replace the database credentials and URL as needed for your environment.

## Usage

Once the application is running, you can access the API at:  
`http://localhost:8080`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

