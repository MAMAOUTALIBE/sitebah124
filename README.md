# rtk-agrncy-blog-web-site
Blog web site

# Deploiement local : avec virtualenv
- [] installer virtualenv : pip install virtualenv venv_name

- [] activer virtualenv : 
        - [] Windows : venv_name\Scripts\activate  
        - [] Ubuntu : source venv_name/bin/activate

- [] installer les dépendances du projet : pip install -r requirements.txt

- [] faire les migrations : 
        - [] python manage.py makemigrations
        - [] python manage.py migrate

- [] lancer le projet : python manage.py runserver
