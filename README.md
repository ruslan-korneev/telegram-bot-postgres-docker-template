# Telegram-Bot-Template
## Stack
Python, Aiogram, Django,
Docker, PostgreSQL
## Setup
```bash
cat env_sample > .env
# change values in .env

docker-compose build
docker-compose up -d
```

## Database migrations
```bash
# to make new migration files
docker-compose exec web sh -c "python3 src/manage.py makemigrations"
# run migrations
docker-compose exec web sh -c "python3 src/manage.py migrate"
```
