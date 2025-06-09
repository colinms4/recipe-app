# Recipe Application

Application where users can enter in recipes to a django database. Entering the name, ingredients, cooking time, and difficulty will store the recipe in the database. User's will be able to create recipes and add them to the database.

# Features 

* Users can authenicate and login to app
* Search for recipes
* Create a recipe
* List of all recipes
* Additional details on recipes

# Technical Stack 
* Backend: Django, SQLite/PostgreSQL
* Frontend: HTML, CSS
* Deployment: Heroku
* Data Visualization: Matplotlib
* Authentication: Django auth system

# Deployment 

Hosted on heroku at https://quiet-taiga-15842-c467ebc30645.herokuapp.com/


## Installation
1. Clone the repo

```
git clone <repository-url>
cd recipe-app
```

2. Create and activate the virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install requirements.txt
```

4. Set up your .env:

```
DEBUG=True
DJANGO_SECRET_KEY=your_secret_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_STORAGE_BUCKET_NAME=your_bucket_name
```

5. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```
6. Create a superuser:
```
python manage.py createsuperuser
```

7. Create required directories:
```
mkdir media
mkdir static
python manage.py collectstatic
```

8. Start the server:
```
python manage.py runserver
```
