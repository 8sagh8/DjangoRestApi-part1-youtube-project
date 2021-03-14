# Project to BUILD OWN APIs using Django RestFramework

* Simple Get Api is created to make new user feel comfortable
* Entire project is based on Python Django Framework
* To access API online, we deployed it on HEROKU
* How to deploy on HEROKU see below:

### Deploy Django Project on HEROKU

* create Github user account: [https://github.com/](https://github.com/)
* create repository on Github
* create Heroku user account: [https://id.heroku.com/login](https://id.heroku.com/login)
* under Deploy => Deployment method => Connect to Github => Search Github Repository
* install Gunicorn
    `pip install gunicorn`
* create 'Procfile' without extension
* add below line in 'Procfile', replace `myproject` with your project name
    `web: gunicorn myproject.wsgi`