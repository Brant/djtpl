#!/usr/bin/env python
import os
import sys
import imp

import django
from django.conf import settings
from django.test.utils import get_runner


MY_INSTALLED_APPS = [
    '{{ project_name }}',
    '{{ project_name }}_tests',
]


try:
    imp.find_module("django_nose")
    MY_INSTALLED_APPS.append("django_nose")
except ImportError:
    pass


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


MY_TEST_RUNNER = 'django.test.runner.DiscoverRunner'

try:
    from django_nose.runner import NoseTestSuiteRunner
    MY_TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
except ImportError:
    pass


if not settings.configured:
    settings.configure(
        BASE_DIR = BASE_DIR,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS = MY_INSTALLED_APPS,
        SITE_ID = 1,
        STATIC_URL = '/static/',
        ROOT_URLCONF = '{{ project_name }}_tests.urls',
        NOSE_ARGS = [
            "--with-xcoverage",
            "--cover-inclusive",
            "--with-xunit",
            "--exe",
            "--verbosity=3",
            "--cover-package={{ project_name }}"
        ],
        NOSE_PLUGINS = [
            'nosexcover.XCoverage',
            "nose_exclude.NoseExclude"
        ],
        TEST_RUNNER = MY_TEST_RUNNER,
    )


def runtests():
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["my_project_tests"])
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests(*sys.argv[1:])
