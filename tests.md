---
title: Test Suite
layout: page
---

The djtpl architecture separates the project test suite from the individual apps. Tests should reside in ```my_project_tests/tests.py```

## To run tests 
{% highlight bash %}
python my_project_tests/runtests.py
{% endhighlight %}

## To enable coverage
{% highlight bash %}
pip install -r my_project_tests/requirements.txt
{% endhighlight %}

Then run tests as above.
