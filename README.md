# Scraper

The **Scraper** project is a Django application for collecting news from [Hacker News](https://news.ycombinator.com/), saving it to a database, and displaying it on a web page using DataTables.

---

## Features

1. **News Collection**  
   The script collects data from Hacker News:
   - Article title (`title`)
   - Link (`link`)
   - Number of points (`points`)
   - Creation date (`created_at`)

2. **Updating Points and Adding New Articles**  
   - Running the `scrape` command again updates the points of existing articles.  
   - New articles are added to the database as new entries.

3. **Console Command**  
   To collect and update data, use the Django management command:
   ```bash
   python manage.py scrape
   ```


## Installation and Setup

1. Clone the repository
https://github.com/aandrjuscenko/hackernews-scraper.git

2. Create a virtual environment and install dependencies
   
**Windows:**
```bash
python -m venv venv       
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

The requirements.txt contains:
Django==6.0.1
requests==2.32.5
beautifulsoup4==4.14.3
mysqlclient==2.2.7

4. Set up MySQL database
   
The project uses the database codnity_db.

Create the database and user:

```sql
CREATE DATABASE codnity_db;

CREATE USER 'codnity_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON codnity_db.* TO 'codnity_user'@'localhost';
FLUSH PRIVILEGES;
```
5. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Collect and update news
```bash
python manage.py scrape
```

7. Run the server
```bash
python manage.py runserver
```

8. Create a Django superuser (for admin access)
```bash
python manage.py createsuperuser
```

9. Tests
The project includes basic unit tests for the Article model.
Django automatically creates and destroys a test database when running tests.

```bash
python manage.py test news
```

## Project Structure

```text
manage.py
requirements.txt
README.md
db.sqlite3
news/
├─ models.py
├─ views.py
├─ urls.py
├─ admin.py
├─ management/
│  └─ commands/
│      └─ scrape.py
└─ templates/
    └─ article_display.html
scraper/
├─ settings.py
├─ urls.py
├─ wsgi.py
└─ asgi.py
```

