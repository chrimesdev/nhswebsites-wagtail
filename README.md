# NHS websites (Wagtail)

## Install and run the application

### Requirements

Wagtail supports Python 3.5, 3.6, 3.7 and 3.8.

To check whether you have an appropriate version of Python 3:

```
python3 --version
```

If this does not return a version number or returns a version lower than 3.5, you will need to install [Python 3](https://www.python.org/downloads/).

### Clone the repository

`git clone https://github.com/AdamChrimes/nhswebsites-wagtail.git nhswebsites` and switch to the project directory `cd nhswebsites`

### Create and activate a virtual environment

We recommend using a virtual environment, which provides an isolated Python environment.

```
pipenv shell
```

### Install project dependencies (Python & npm)

Python dependencies

```
pip3 install -r requirements.txt
``` 

npm dependencies

```
npm install
```

### Create the database

```
python3 manage.py migrate
```

### Create an admin user

```
python3 manage.py createsuperuser
```

### Start the server

```
npm run watch
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) and you can access the administrative area at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
