from django.core.management.base import BaseCommand
from scraper.quote_scraper import scrape_quotes


class Command(BaseCommand):
    help = 'Scrape quotes from http://quotes.toscrape.com and save to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting quote scrape...")
        scrape_quotes()
        self.stdout.write("Scraping complete.")
