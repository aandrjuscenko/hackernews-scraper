# Scraper

Проект **Scraper** — это Django-приложение для сбора новостей с [Hacker News](https://news.ycombinator.com/), сохранения их в базу данных и отображения на веб-странице с использованием DataTables.  

---

## Функционал

1. **Сбор новостей**: Скрипт собирает данные с Hacker News:
   - Заголовок статьи (`title`)
   - Ссылка (`link`)
   - Количество очков (`points`)
   - Дата создания (`created_at`)  

2. **Обновление очков и добавление новых статей**:  
   - При повторном запуске команды `scrape.py` обновляются очки существующих статей.  
   - Если появляются новые статьи, они добавляются в базу как новые записи.  

3. **Консольная команда**: Для сбора и обновления данных используется Django management command с именем:

python manage.py scrape


Установка и запуск
1. Клонирование репозитория
https://github.com/aandrjuscenko/hackernews-scraper.git

2. Создание виртуального окружения и установка зависимостей

# Windows:
python -m venv venv         # создаём своё виртуальное окружение
venv\Scripts\activate

# Установка библиотек
Pip installs:
Django==6.0.1
requests==2.32.5
beautifulsoup4==4.14.3
mysqlclient==2.2.7

3. Настройка базы данных MySQL

Проект использует базу данных **codnity_db**.  

Создайте базу данных:

```sql
CREATE DATABASE codnity_db;

CREATE USER 'codnity_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON codnity_db.* TO 'codnity_user'@'localhost';
FLUSH PRIVILEGES;

В файле Scraper/settings.py указаны настройки подключения:

4. Применение миграций
python manage.py makemigrations
python manage.py migrate

5. Сбор и обновление новостей
python manage.py scrape

6. Запуск сервера
python manage.py runserver

Главная страница (`/`) **отображает таблицу со всеми новостями**.  
Данные обновляются и добавляются **только при запуске команды**:



Scraper/
├─ Scraper/         # Настройки Django
├─ News/            # Приложение News
│  ├─ models.py     # Модель Article
│  ├─ views.py      # Получение данных и рендер на страницу
│  ├─ templates/
│  │  └─ news_list.html  # Шаблон с DataTables
│  └─ management/
│     └─ commands/
│        └─ scrape.py  # Команда для сбора и обновления данных
└─ README.md

## Tests

Django automatically creates and destroys a test database when running tests.

To run tests:

python manage.py test news

