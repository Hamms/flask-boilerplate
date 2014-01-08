Flask Boilerplate
==================

This is a barebones [Flask] project. Feel free to use it as a launching ground for your own little projects.

Version
-------

1.0

Requirements
------------

This project assumes and suggests you use [pip], [virtualenv] with [virtualenvwrapper], and [PostgreSQL]


Tech
----

This project uses a number of open source libraries:

* [Flask] - a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [SQLAlchemy] - SQL toolkit and Object Relational Mapper
* [Alembic] - a lightweight database migration tool for usage with SQLAlchemy 
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [HTML5 Boilerplate] - a professional front-end template for building fast, robust, and adaptable web apps or sites

Installation
------------

```sh
git clone [git-repo-url] [project-name]
cd [project-name]
mkvirtualenv [project-name]
pip install -r requirements.txt
psql -h localhost -c "create database [database-name]"
cp config_local.py.example config_local.py
echo "SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/[database-name]'" >> config_local.py
./manage.py migrate upgrade head
```

Usage
-----

```sh
./manage.py runserver
```

Then visit [http://localhost:8000](http://localhost:8000) in your browser of choice.

License
-------

MIT

*Free Software, Fuck Yeah!*

[Alembic]:alembic.readthedocs.org
[Flask]:flask.pocoo.org
[HTML5 Boilerplate]:html5boilerplate.com
[PostgreSQL]:http://www.postgresql.org
[SQLAlchemy]:www.sqlalchemy.org
[Twitter Bootstrap]:http://twitter.github.com/bootstrap/
[pip]:https://pypi.python.org/pypi/pip
[virtualenv]:http://www.virtualenv.org/
[virtualenvwrapper]:http://virtualenvwrapper.readthedocs.org/en/latest/

