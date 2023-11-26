python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --noinput
python manage.py init_admin
python manage.py runserver 0.0.0.0:8000