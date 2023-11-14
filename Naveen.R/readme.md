>django-admin --version
<!-- my path (base) C:\1 My Work\django\Naveen.R\telusko> -->

    # List all the environments
    conda env list
    # alternate syntax
    conda info --envs
    # activate the venv
    activate <env_name>
    workon <env_name>

>django-admin startproject telusko

>cd telusko

>python manage.py runserver

----------------------
<br>

flow --> website url-->url.py--->views.py--->template--->models.py



>python manage.py startapp calc
- include calc(app) name inside settings.py==> **INSTALLED_APPS**
- create urls.py file in folder(app) name calc
- write code in urls.py and later in views.py of app
- Also include urls.py(app) inside urls.py(project)

------------

- Create **templates** folder in home directory
- add variable for inculding template folder in settings.py
- now change views.py pointing to html files present in templates folder
- for dynamic template we can use {{key}} and sepecify the {k:v} in views.py as *content*
- some time base theme will be same for all the web-pages, so u can include 1-html inside other html.
-----------------

<br>






<br>
<br>
<br>

##  Notes:

1) In *Settings.py* don't share **SECRET_KEY** and make **DEBUG = False** in production
2)