# Web Scraping Tool with FastAPI

## Overview

This project is a web scraping tool built using the FastAPI framework. It scrapes product information from `dentalstall` website and stores it in an SQLite database. The tool also includes features such as basic authentication, retry mechanism, and caching using Redis.


## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- Redis
- Pydantic
- SQLAlchemy
- SQLite
- Unittest

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/atul107/dentalstall-scraper
   cd dentalstall-scraper
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate 
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI server:**

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Scrape products:**

   Make a GET request to the `/scrape` endpoint with optional query parameters `pages` and `proxy`:

   ```
   GET /scrape?pages=5&proxy=http://yourproxy:port
   ```

3. **Authentication:**

   Use basic authentication with the static token as the password.

## Testing

Run the tests using `unittest`:

```bash
python -m unittest discover tests
```
