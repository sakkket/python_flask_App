# Python Flask App

Python flask application to fetch data from multiple databases(MySQL and PostgreSQL) using sqlalchemy.

## Libraries used

```bash
Python:- 3.8.5
flask:- 1.1.2
sqlalchemy:- 1.3.23
Python MySQL client:- PyMySQL
```

## Description

```bash
userEntity:- contains the table mapping
controller:- core file with database connection string, engine and API routes
env:- contains credentials for MySQL and PostgreSQL databases
```

## Running the app

```bash
$ export FLASK_APP=controller.py
$ flask run
```

## env file contents

```bash
mysql_db = 'user'
mysql_username = 'root'
mysql_password = 'mysqlpwd'
mysql_port = '3306'


postgresql_db = 'library'
postgresql_username = 'root'
postgresql_password = 'postgrespwd'
postgresql_port = '5432'
```
