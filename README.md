![PyPI - Python Version](https://img.shields.io/badge/Python-3.7-brightgreen)
![PyPI - Python Version](https://img.shields.io/badge/Django-3.1-green)
![PyPI - Python Version](https://img.shields.io/badge/requirements.txt-updated-yellow)
# MovieRating
## Purpose of Plan
The project was undertaken to illustrate the knowledge of Nosql in particularMongodb, which is a Document-Based database.
Over the past few years, large tech companies such as Netflix, Hulu, Uber and Facebook and have brought notoriety to
NoSQL or non-relational databases. In our project we will give a brief introduction to the types of
NoSQL(especially mongodb) databases and how they compare to traditional SQL databases.

The key difference between a NoSQL and SQL is that a SQL database isconsidered a relational database. A relational
database stores data in tables, which are organized into columns. Each column stores one datatype (integer,real number,
string, date etc.) and each row represents an instance of thetable. Non-relational databases do not store data in
tables- instead there are multiple ways to store data in NoSQL databases (Key-value, Document-based, Column-based).

## Preview
![Project Preview](https://github.com/mopidevimu/MovieRating/blob/master/git-images/ezgif.com-gif-maker.gif)

## Usage

```python
STEP-1

# Install MongoDB Database
# Download and  install MongoDB latest version as backend from the below URL
    URL :- https://www.mongodb.com/download-center/community

# Install All required Packages

    pip install -r requirements.txt

STEP-2

# Delete Migrations files which are already availble in "migrations" folders in Apps like "users", "rating".
# Example:-
# MovieRating/users/migrations/0001_initial.py
# MovieRating/rating/migrations/0001_initial.py
# MovieRating/rating/migrations/0002_auto_20200317_1358.py
# Open Command Promt inside the Project Main Folder " MovieRating/----> Here "
    i) python manage.py makemigrations

# note:- The above command create the the migration file for all models(Tables)
# which are written models.py files in Project.

    ii) python manage.py migrate

# note:- It creates the all Tables in maongodb.(as per ur DATABASE SETTINGS).

    iii) python manage.py createsuperuser

# note:- The above command asks about
# Username:
# Email:
# paswword:
# confirm password:

# Example:-
# Username:user
# Email:user@user.eu
# paswword:azert123
# confirm password:azert123
# just provied your details for loging as admin to the website.

STEP-3

# Then run project by using the below command

     python manage.py runserver

 # note:- if the above command execute it give an url for opening website
    URL http://127.0.0.1:8000/

STEP-4

# Initially in website don't have any information like RATING, OPINIONS, MOVIES INFORMATIONS.
# "so we need to login as admin then import data into database from CSV folder.
# for importing data goto the below link and login as a superuser crediantial's which is

# you already created in above STEP-2 --> iii)"

    URL http://127.0.0.1:8000/admin

STEP-5

# login to website and import the CSV files from CSV(FOLDER)
# i)first upload ratingss table
# ii)seconnd uplaod opinions tables
# iii)third upload movies table
# and logout from admin panel.

STEP-6

# Then go to below url for Website.
  URL http://127.0.0.1:8000/

# you can find the movies info in movies menu
# then click in login and login with same crediantials.
# and create a review.

STEP-7

# For forget password we need to add email and password at
# MovieRating/MovieRating/settings.py file
# end of the settings you need to change these 2 lines like this

    EMAIL_HOST_USER = 'youremailid@gmgg.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'

# Instead of these below lines

    EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

```