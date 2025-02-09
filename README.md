# Number Classification API

A REST API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides number properties (odd/even, armstrong)
- Fetches fun facts about numbers from Numbers API

## Quick Start

The easiest way to get started is to visit the root endpoint `/` which will provide you with the API information:

```json
{
  "message": "Welcome to the Number Classification API",
  "endpoint": "/api/classify-number",
  "example": "/api/classify-number?number=371",
  "documentation": "See README.md for more details"
}
```

This welcome message provides:

- The main endpoint for number classification
- A working example you can try
- Reference to this documentation

## API Specification

### Endpoints

#### 1. Root Endpoint (Welcome Page)

```
GET /
```

Returns basic API information and available endpoints. This is the best starting point for new users.

Response example:

```json
{
  "message": "Welcome to the Number Classification API",
  "endpoint": "/api/classify-number",
  "example": "/api/classify-number?number=371",
  "documentation": "See README.md for more details"
}
```

#### 2. Number Classification Endpoint

```
GET /api/classify-number?number={number}
```

Parameters:

- `number` (required): Integer value to analyze

Success Response (200 OK):

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

Error Response (400 Bad Request):

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
4. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Visit http://localhost:8000/ to see the welcome message

### Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `./build.sh`
   - Start Command: `gunicorn one.wsgi:application`
4. Deploy!
5. Visit your deployed URL to see the welcome message

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
- Helpful welcome page with example endpoint

## Examples

1. Check Armstrong number:

```
GET /api/classify-number?number=371
```

2. Check Prime number:

```
GET /api/classify-number?number=17
```

3. Check Perfect number:

```
GET /api/classify-number?number=28
```

## Testing the API

1. Start with the root endpoint (`/`) to verify the API is running
2. Use the example URL provided in the welcome message
3. Try different numbers to explore various mathematical properties

## License

MIT
