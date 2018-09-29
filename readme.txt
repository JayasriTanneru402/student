virtualenv -p python3 myenvs
. myenvs/bin/activate
pip install django pillow coverage django-jenkins 
python manage.py makemigrations
python manage.py migrate
python manage.py jenkins --enable-coverage
