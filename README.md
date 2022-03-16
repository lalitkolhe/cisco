# cisco_assignment

#environment
#python -m venv /c/Users/user/Documents/Assignment_Lalit/env
#source /c/Users/user/Documents/Assignment_Lalit/env/Scripts/activate

Location 
> cd project_Q1

Libraries that needs to be install are as follows:-
> pip install -r requirements.txt
> winpty python manage.py createsuperuser

commands needed to build and run the application are as follows:-
1)python manage.py makemigrations - to make migration

2)python manage.py migrate - model creation

3)python manage.py runserver - run django server

###Api
http://127.0.0.1:8000/all - GET call - to display all routers

http://127.0.0.1:8000 - POST
{
    "Sapid": 123,
    "Hostname": "host1",
    "Loopback": "10.10.10.1"
}