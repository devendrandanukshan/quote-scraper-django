import requests
import csv
from bs4 import BeautifulSoup
from .models import Quote

BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
    page = 1
    csv_file = open('scraped_quotes.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['Text', 'Author', 'Tags'])  # Header row

    while True:
        url = f"{BASE_URL}/page/{page}/"
        response = requests.get(url)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quote_divs = soup.find_all('div', class_='quote')
        if not quote_divs:
            break

        for div in quote_divs:
            text = div.find('span', class_='text').get_text(strip=True)
            author = div.find('small', class_='author').get_text(strip=True)
            tags = ",".join([tag.get_text(strip=True) for tag in div.find_all('a', class_='tag')])

            # Save to database if not duplicate
            if not Quote.objects.filter(text=text, author=author).exists():
                Quote.objects.create(text=text, author=author, tags=tags)
                print(f"✅ Added to DB: {text[:60]}...")

            # Always save to CSV (even if already in DB)
            writer.writerow([text, author, tags])
            print(f"📦 Saved to CSV: {text[:60]}...")

        page += 1

    csv_file.close()
    print("📁 CSV export completed: scraped_quotes.csv")
