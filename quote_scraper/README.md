# 🧠 Quote Scraper Django – Python Web Scraper

A Django-based scraper that extracts quotes from [http://quotes.toscrape.com](http://quotes.toscrape.com), stores them in a PostgreSQL/SQLite database, and exports them into CSV and JSON files for structured use.

## 🔧 Features

- Django-powered backend
- CLI trigger with `manage.py scrape`
- BeautifulSoup for HTML parsing
- Output saved as `quotes.csv` and `quotes.json`
- Reusable command structure for future scrapers

## 📦 Stack

- Python
- Django
- BeautifulSoup
- SQLite (or PostgreSQL-ready)
- CSV & JSON module

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the scraper
python manage.py scrape
