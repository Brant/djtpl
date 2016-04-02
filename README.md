djtpl: A Project Template for Django
====================================

*Updated for Django 1.9*

djtpl is a rather opinionated start to a new Django project. It includes a few things so that you don’t have to worry about dealing with them in order to get up and running.

## Quickstart
You'll need [virtualenv](http://virtualenv.readthedocs.org/en/latest/) installed first.

```
virtualenv env
. ./env/bin/activate
pip install django
django-admin.py startproject my_project --template=https://github.com/Brant/djtpl/archive/master.zip
pip install -r my_project/requirements.txt
```

## Documentation
For more information, check out the [documentation](http://brant.github.io/djtpl/)
