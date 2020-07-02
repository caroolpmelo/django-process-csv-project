# Django "Process CSV" Project

A basic Django project that creates two apps, each one with one model, and one of them reads a CSV file to insert data to the other one.

<br>

### Apps:

- processo
  - model: 'Processo'
  - attributes: [ pasta (String), comarca (String), uf (String) ]

* cadastro_processo
  - model: 'Planilha'
  - attributes: [ nome (String), cliente (String), arquivo (FileField) ]

#### When one new 'Planilha' is created ('arquivo' field is required), it also creates a new 'Processo' register per line of the CSV file.

<br>

### Versions:

    Python 3.6.9
    Django 2.2.14 (LTS)
    *other dependecies are listed on requirements.txt

To install other dependencies: `pip install -r requirements.txt`

<br>

#### How to create database and superuser:

`python manage.py migrate`

`python manage.py createsuperuser` # asks for user and password for admin registration

<br>

#### How to run project:

`python manage.py runserver`

<br>

Acess admin panel via `localhost/admin` (if localhost) or `...URL.../admin` (if Heroku)

<br>

Heroku: (note that for superuser register, Heroku CLI is needed locally)

https://django-process-csv-project.herokuapp.com/
