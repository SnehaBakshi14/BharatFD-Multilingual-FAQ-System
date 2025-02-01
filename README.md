# Multilingual FAQ System (Django)

A robust Django-based FAQ management system supporting multiple languages, automatic translation, Redis caching, and an optimized RESTful API for seamless interactions.

## Key Features

 - ✔️ Full CRUD functionality for FAQ management
 - ✔️ Automatic language translation via Google Translate API
 - ✔️ High-speed performance with Redis caching
 - ✔️ Supports multiple languages, including English, Hindi, and Bengali
 - ✔️ RESTful API with language-based filtering for easy data retrieval
 - ✔️ Django Admin integration for streamlined FAQ management
 - ✔️ Effortless deployment using Docker

---

## Installation

### Using Docker (Preferred Method)

Ensure that Docker and Docker Compose are installed, then execute:

```bash
docker-compose up -d
```

### Manual Setup

1. **Clone the Repository:**

```bash
git clone <repo-url>
cd multilingual-faq-system
```

2. **Create and Activate a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply Database Migrations:**

```bash
python manage.py migrate
```

5. **Start Redis Server:** (Ensure Redis is installed on your system)

```bash
redis-server
```

6. **Run the Development Server:**

```bash
python manage.py runserver
```

Access the API at: `http://127.0.0.1:8000/api/faqs/`

---

## API Documentation

The interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

### Available Endpoints

| Method | Endpoint     | Description                           |
|--------|-------------|---------------------------------------|
| POST   | `/api/faqs/` | Create a new FAQ                      |
| GET    | `/api/faqs/` | Retrieve FAQs with language filtering |

### Example API Calls

**Creating a New FAQ:**

```bash
curl -X POST "http://127.0.0.1:8000/api/faqs/" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Django?", "answer": "Django is a high-level Python web framework."}'
```

**Fetching FAQs in Hindi:**

```bash
curl "http://127.0.0.1:8000/api/faqs/?lang=hi"
```

---

## Configuration

Set up the following environment variables in a `.env` file:

```
DJANGO_SECRET_KEY=your_secret_key
REDIS_URL=redis://127.0.0.1:6379/1
```

---

## Running Tests

Execute tests using:

```bash
pytest
```

Check PEP8 compliance:

```bash
flake8 .
```

---

## Deployment Guide

### Deploying with Docker

Ensure Docker is installed, then run:

```bash
docker build -t multilingual-faq .
docker run -p 8000:8000 multilingual-faq
```

### Deploying to Heroku (If Required)

```bash
git push heroku main
```

---

## Contribution Guidelines

1. Fork the repository
2. Create a new branch for your feature
3. Implement changes and commit with clear messages
4. Push to your branch
5. Open a Pull Request

---

## Git Commit Conventions

Use structured commit messages:

- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching logic`
- `docs: Update API usage in README`

Ensure each commit is concise and well-documented.

---

## License

This project is licensed under the MIT License.