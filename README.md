## Dartblog
Blog with the ability to register an account and comments, https://indiora.pythonanywhere.com/

# Local deployment
1. Download project
2. docke-compose build
3. docker-compose run blog python manage.py makemigrations
4. docker-compose run blog python manage.py migrate
5. docke-compose up
