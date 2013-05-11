My Django Project Starter
-------------------------

django-admin.py startproject &lt;project_name&gt; --template=https://github.com/Brant/djtpl/archive/master.zip

Test Suite
---------
This project architecture separates the project test suite from the individual apps. Tests should reside in the {{ project_name }}_tests.tests.py.

To run tests, do `python my_project_tests.runtests.py`

To enable coverage, install my_project_tests/requirements.txt
