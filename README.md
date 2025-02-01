# Multilingual FAQ System (Django)

A Django-based system for managing multilingual FAQs with automatic translation, WYSIWYG editor support, Redis caching, and an optimized RESTful API.

## Features

- Perform CRUD operations for FAQs
- Automate translation via Google Translate API
- Implement Redis caching for faster performance
- Support multiple languages (English, Hindi, Bengali, etc.)
- Provide a RESTful API with language-based query parameters
- Integrate Django Admin for FAQ management
- Offer Docker support for easy deployment

---

## Installation

### Using Docker (Recommended)

Ensure Docker and Docker Compose are installed, then run :-

```bash
docker-compose up -d
```

### Manual Setup

1. **Clone the Repository:**

```bash
git clone <repo-url>
cd multilingual-faq-system
```

2. **Set Up a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # for linux users
venv\Scripts\activate  # for windows users
```

3. **Install Required Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply Database Migrations:**

```bash
python manage.py migrate
```

5. **Start Redis Server:** (Ensure Redis is installed)

```bash
redis-server
```

6. **Run the Development Server:**

```bash
python manage.py runserver
```

API will be accessible at: `http://127.0.0.1:8000/api/faqs/`

---

## API Documentation

The API provides a fully interactive documentation interface at:

```
http://127.0.0.1:8000/docs
```

### Available Endpoints

| Method | Endpoint     | Description                           |
| ------ | ----------- | ------------------------------------- |
| POST   | `/api/faqs/` | Create a new FAQ                      |
| GET    | `/api/faqs/` | Retrieve FAQs with language selection |

### Example Usage

**Creating a New FAQ:**

```bash
curl -X POST "http://127.0.0.1:8000/api/faqs/" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Django?", "answer": "Django is a high-level Python web framework."}'
```

**Retrieving FAQs in Hindi:**

```bash
curl "http://127.0.0.1:8000/api/faqs/?lang=hi"
```

---

## Configuration

Set the following environment variables in a `.env` file:

```
DJANGO_SECRET_KEY=your_secret_key
REDIS_URL=redis://127.0.0.1:6379/1
```

---

## Running Tests

Execute tests with:

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

Ensure Docker is installed, then execute:

```bash
docker build -t multilingual-faq .
docker run -p 8000:8000 multilingual-faq
```

### Deploying on Heroku (If Anybody wants to)

```bash
git push heroku main
```

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your modifications and commit using descriptive messages
4. Push your changes
5. Open a Pull Request

---

## Git Best Practices

Follow structured commit messages:

- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API details`

Ensure each commit is atomic and well-documented.

---

## License

Distributed under the MIT License.
