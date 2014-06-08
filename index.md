---
title: djtpl&#58; A Project Template for Django
layout: page
body_class: home
---

djtpl is a rather opinionated start to a new Django project. It includes a few things so that you don't have to worry about dealing with them in order to get up and running.

- Project structure including templates area, static files area (css and js), and test suite
- CSS and JS minifier (for development *and* production)
- Base HTML template based on the [HTML5 boilerplate](http://html5boilerplate.com/)
- Some Django apps pre-installed

The goal is to get a new Django project up and running as quickly as possible, without having to fiddle with a lot of configurations or directory structuring each time.

## Quickstart

{% highlight bash %}
virtualenv env
. ./env/bin/activate
pip install django
django-admin.py startproject my_project --template=https://github.com/Brant/djtpl/archive/master.zip
pip install -r my_project/requirements.txt
{% endhighlight %}

In the above example, `my_project` can be replaced by whatever you want your project to be called.

Next, take a look at the [pre-configured features]({{ "/features/" | prepend : site.baseurl }}) offered in djtpl.
