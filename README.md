git clone <git@github.com:sireesbrl/django_blog.git>

cd django_blog/

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

create a .env file in root directory
  - EMAIL_HOST_USER
  - EMAIL_HOST_PASSWORD
  - DEFAULT_FROM_EMAIL
  - SECRET_KEY
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
  - DB_HOST

after installing a postgres database: python3 manage.py migrate
python3 manage.py runserver
