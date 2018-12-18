{{ project_name|title }} Quick Start
====================================

Below you will find basic setup and deployment instructions for the {{ project_name }}
project. To begin you should have the following applications installed on your
local development system:

- Python >= 3.6
- Postgres >= 9.6
- git


Getting Started
---------------

First clone the repository from Github and switch to the new directory::

    $ git clone git@github.com:[ORGANIZATION]/{{ project_name }}.git
    $ cd {{ project_name }}

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    # Check that you have python3.6 installed
    $ which python3.6
    $ mkvirtualenv {{ project_name }} -p `which python3.6`
    ({{ project_name }})$ make dev

Configurable settings are managed with `django-dotenv <https://github.com/jpadilla/django-dotenv>`_.
It reads environment variables located in a file name ``.env`` in the top level directory of the project.
The previous command ``make dev`` creates new ``.env`` file with a new ``SECRET_KEY`` value set.

Create the Postgres database and run the initial migrate::

    ({{ project_name }})$ createdb -E UTF-8 {{ project_name }}
    ({{ project_name }})$ python manage.py migrate

You should now be able to run the development server::

    ({{ project_name }})$ python manage.py runserver


Testing
-------

The ``Makefile`` for this project has a number of helpful commands for testing
and checking code quality. Below is a brief description of the commands

- ``make test`` - Runs the full test suite and reports test coverage
- ``make lint`` - Runs a set of subcommands to check code quality
 - ``make lint-py`` - Runs the code through ``flake8`` for static analysis
 - ``make lint-migrations`` - Runs Django's checks for model changes without migrations
 - ``make lint-django`` - Runs Django's system checks with the base settings
 - ``make lint-deploy`` - Runs Django's system checks for deployment
