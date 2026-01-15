# news/management/commands/scrape.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from news.models import Article
from datetime import timedelta
import re
from django.utils import timezone


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "https://news.ycombinator.com/"
        self.stdout.write(f"Fetching {url} ...")
        # print(f"Fetching {url} ...")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(f"Error fetching the page: {e}")
            # print(f"Error fetching the page: {e}")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # Finding all records with articles
        rows = soup.select("tr.athing")
        for row in rows:
            try:
                # Title and main link
                title_tag = row.select_one("span.titleline > a")
                if not title_tag:
                    continue  # if not title we skip
                title = title_tag.get_text()
                link = title_tag['href']
                if not link.startswith("http"):
                    link = f"https://news.ycombinator.com/{link}"

                # Articles id for searching subtext
                article_id = row['id']
                subtext_row = row.find_next_sibling("tr")
                subtext = subtext_row.select_one("td.subtext") if subtext_row else None
                if not subtext:
                    continue

                # Scores
                points_tag = subtext.select_one("span.score")
                points = int(points_tag.get_text().split()[0]) if points_tag else 0

                # Date created
                time_tag = subtext.select_one("span.age > a")
                created_at = timezone.now() 
                if time_tag:
                    text = time_tag.get_text().strip()
                    match = re.match(r"(\d+)\s+(minute|hour|day)s?\s+ago", text)
                    if match:
                        value, unit = match.groups()
                        value = int(value)
                        if unit == "minute":
                            created_at = timezone.now() - timedelta(minutes=value)
                        elif unit == "hour":
                            created_at = timezone.now() - timedelta(hours=value)
                        elif unit == "day":
                            created_at = timezone.now() - timedelta(days=value)

                # Creating ot uodating articles
                article, created = Article.objects.get_or_create(
                    link=link,
                    defaults={
                        'title': title,
                        'points': points,
                        'created_at': created_at,
                    }
                )
                if not created:
                    # Updating score for existing articles
                    article.points = points
                    article.save()

                self.stdout.write(f"{'Created' if created else 'Updated'}: {title} ({points} points)")
                # print(f"{'Created' if created else 'Updated'}: {title} ({points} points)")

            except Exception as e:
                self.stderr.write(f"Error processing row: {e}")
                # print(f"Error processing row: {e}")

        self.stdout.write("Scraping is completed!")
        # print("Scraping is completed!")
