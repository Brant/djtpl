My Django Project Starter
-------------------------

```
virtualenv env
pip install django
django-admin.py startproject my_project --template=https://github.com/Brant/djtpl/archive/master.zip
pip install -r my_project/requirements.txt
```

Test Suite
----------
This project architecture separates the project test suite from the individual apps. Tests should reside in my_project_tests/tests.py

###To run tests 
`python my_project_tests.runtests.py`

###To enable coverage
`pip install -r my_project_tests/requirements.txt`
