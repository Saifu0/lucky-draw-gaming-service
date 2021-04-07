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

# API Documentation and testing 
Once the development server is up and running then you can visit http://127.0.0.1:8000/swagger/ to see API documentation.

## Endpoints response screenshots

1. Getting tickets for a user ( By default : 2 Tickets ) 

http://127.0.0.1:8000/api/tickets/<user_id> 

e.g. http://127.0.0.1:8000/api/tickets/3
![image](https://user-images.githubusercontent.com/43892879/113885992-f17d0100-97dd-11eb-9718-8b92ef041213.png)

Tickets with count, http://127.0.0.1:8000/api/tickets/2?count=5

![image](https://user-images.githubusercontent.com/43892879/113886395-44ef4f00-97de-11eb-9075-2cdc5fff50ca.png)
