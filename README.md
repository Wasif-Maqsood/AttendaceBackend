# AttendaceBackend
Python 3.10
Install Postgres and make database fullappbackend

Create new environment
Goto AttendanceBackend Folder
pip install -r requirements/base.txt
Goto config/setting.py change database username and password

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
add email username and password

python manage.py runserver
