# Project to BUILD OWN APIs using Django RestFramework

* Simple Get Api is created to make new user feel comfortable
* Entire project is based on Python Django Framework
* To access API online, we deployed it on HEROKU
* How to deploy on HEROKU see below:

### Deploy Django Project on HEROKU

* create Github user account: [https://github.com/](https://github.com/)
* create repository on Github
* create Heroku user account: [https://id.heroku.com/login](https://id.heroku.com/login)
* install Heroku CLI: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
* under Deploy => Deployment method => Connect to Github => Search Github Repository
* install Gunicorn
    `pip install gunicorn`
* create 'Procfile' without extension
* add below line in 'Procfile', replace `myproject` with your project name
    `web: gunicorn myproject.wsgi`
* pip install django-heroku
* create requirments file using following command
    `pip freeze > requirements.txt` 
* NOTE: after deploying on heroku, if any python library | frameworks' version is not compatible with Heroku then install supportive version or remove it from file if not necessary for project.
* add import statement in settings.py
    `import django_heroku`
* at the bottom of settings.py add below
    `django_heroku.settings(locals())`
* change debug setting in settings.py
    `DEBUG = False` OR use below code

`if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):`
    `DEBUG = True`
`else:`
    `DEBUG = False`
    
* run below for heroku
    `heroku run python manage.py migrate`
* create super user for heroku
    `heroku run python manage.py createsuperuser`