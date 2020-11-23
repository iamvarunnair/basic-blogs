# basic-blogs

A basic blog website with a list of blogs, single blog view and a back office user account with login, logout, blog lit view add blogs and delete blogs.

### Features

-   Blog list - A list of all bogs in a card layout with an image, title, short description and button to see single blog view.
-   Single blog view - A full view of a single blog

A back office user login

-   Login - User can login to manage blogs, registration needs to be done through django admin or directly in database.
-   Blog List - List of all created blogs and a feature to delete them.
-   Add Blog - An add blog form with a title, and dyanmic form to add a subsequent list of paragraphs with an image and text for each paragraph.

### Tech

-   [Python](python.org)
-   [Django](djangoproject.com)
-   [Django Rest Framework](django-rest-framework.org)
-   [Bootstrap](getbootstrap.com)
-   [Scss](sass-lang.com)

### Installation

Create a python environment. You can use virtualenvwrapper or virtualenvwrapper-win(for windows) following this:

```sh
mkvirtualenv -r requirements.txt <your env name>
```

Set up django admin

```sh
$ py manage.py makemigrations
$ py manage.py migrate
$ py manage.py createsuperuser
```

Login on localhost:8000/admin with the super user and fill all status table with two entries 1) Active and 2) Inactive in the same order.

Add a back office user.

```sh
localhost:8000/ - To view public blog list.
localhost:8000/BO - To login back office user.
```

### To Do

-   Use Jinga2 templae engine.
-   Use management command to fill all static tables.
