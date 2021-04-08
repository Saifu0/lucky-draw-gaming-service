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

# Database Schema and relationships
![Screenshot (9)](https://user-images.githubusercontent.com/43892879/113990243-e0c89b80-986e-11eb-828b-3c7e9c8a0579.png)


# API Documentation and automated testing 
Once the development server is up and running then you can visit http://127.0.0.1:8000/swagger/ to see API documentation.

###### Models and Views(API) automated testing
```
python manage.py test
```

## Endpoints response screenshots

1. GET method: Getting tickets for a user ( By default : 2 Tickets ) 

http://127.0.0.1:8000/api/tickets/<user_id>  e.g. http://127.0.0.1:8000/api/tickets/3

![image](https://user-images.githubusercontent.com/43892879/113885992-f17d0100-97dd-11eb-9718-8b92ef041213.png)

Tickets with count, http://127.0.0.1:8000/api/tickets/2?count=5

![image](https://user-images.githubusercontent.com/43892879/113886395-44ef4f00-97de-11eb-9075-2cdc5fff50ca.png)

2. GET method: Getting list of upcoming events

http://127.0.0.1:8000/api/upcoming-events

![image](https://user-images.githubusercontent.com/43892879/113886867-a1eb0500-97de-11eb-92d6-a38baccdd28a.png)

3. POST method: Participating in an event ( event_id and ticket_id required in body)

http://127.0.0.1:8000/api/participate
```
Body
{
	"event_id" : 5,
	"ticket_id" : 7
}

```
![image](https://user-images.githubusercontent.com/43892879/113887404-158d1200-97df-11eb-8bc5-84c3fb343efb.png)

4. GET method: Get all past winners

http://127.0.0.1:8000/api/past-winners

![image](https://user-images.githubusercontent.com/43892879/113887902-803e4d80-97df-11eb-8b0a-055b484b4391.png)

5. GET method: Announce winner of an event. ( event_id is required )

http://127.0.0.1:8000/api/event-winner/<event_id> e.g. http://127.0.0.1:8000/api/event-winner/6

![image](https://user-images.githubusercontent.com/43892879/113888481-03f83a00-97e0-11eb-9f64-4db4958c73c3.png)

