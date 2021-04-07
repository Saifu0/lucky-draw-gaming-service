# Setting Up locally
* Install `pipenv` using command `pip install pipenv`
* Clone the repository.
* Activate virtual environment using command `pipenv shell`
* Install all dependecies using command `pipenv install`
* Navigate to the `server` directory and type
```
python manage.py migrate
```
* Create super user to access admin dashboard
```
python manage.py createsuperuser
```
* Start the development server
```
python manage.py runserver
```
* Open `127.0.0.1:8000` into the browser to see things in action
