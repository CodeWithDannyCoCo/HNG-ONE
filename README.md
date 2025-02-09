# Number Classification API

A REST API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides number properties (odd/even, armstrong)
- Fetches fun facts about numbers from Numbers API

## API Specification

### Endpoint

```
GET /api/classify-number?number={number}
```

### Success Response (200 OK)

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)

```json
{
  "number": "alphabet",
  "error": true,
  "message": "Invalid number format"
}
```

## Setup and Installation

### Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `./build.sh`
   - Start Command: `gunicorn one.wsgi:application`
4. Deploy!

## Dependencies

- Django
- Django REST Framework
- django-cors-headers
- requests
- gunicorn (for production)
- whitenoise (for static files)

## Features

- CORS enabled
- Error handling
- Input validation
- Fast response time
- RESTful API design
- Production-ready configuration
- Static file serving with whitenoise

## License

MIT
