# NHS websites (Wagtail)

## Running the application

```
git clone https://github.com/AdamChrimes/nhswebsites-wagtail.git nhswebsites
cd nhswebsites
pipenv shell
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
