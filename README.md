# Number Classification API

A REST API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides number properties (odd/even, armstrong)
- Fetches fun facts about numbers from Numbers API

## Base URL

```
https://hng-one-iiyg.onrender.com
```

## API Specification

### Endpoints

#### 1. Root Endpoint

```
GET /
```

Returns a simple welcome message.

Response example:

```json
{
  "message": "Number Classification API"
}
```

#### 2. Number Classification Endpoint

Base endpoint (for submission):

```
GET /api/classify-number
```

To use the API (with query parameter):

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
  "fun_fact": "371 is a narcissistic number"
}
```

Error Responses:

1. Missing Number Parameter (400 Bad Request):

```json
{
  "error": true,
  "message": "Please provide a number parameter"
}
```

2. Invalid Number Format (400 Bad Request):

```json
{
  "error": true,
  "message": "Invalid number format"
}
```

3. Server Error (500 Internal Server Error):

```json
{
  "error": true,
  "message": "Internal server error"
}
```

## Important Note for Submission

When submitting the API endpoint for evaluation, use only the base endpoint without query parameters:

```
https://hng-one-iiyg.onrender.com/api/classify-number
```

DO NOT include:

- Query parameters (e.g., `?number=371`)
- Trailing slashes
- Additional paths

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

## Features

- CORS enabled
- Error handling
- Input validation
- Fast response time
- RESTful API design
- Production-ready configuration

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
2. Test the number classification endpoint:
   - Without parameters (should return 400)
   - With invalid number (should return 400)
   - With valid number (should return 200)
3. Verify all responses match the specified formats above

## License

MIT
