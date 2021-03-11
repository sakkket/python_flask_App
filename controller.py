from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from userEntity import User
from userEntity import Book
import os
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

# mysql credentials
mysql_db = os.getenv('mysql_db')
mysql_username = os.getenv('mysql_username')
mysql_password = os.getenv('mysql_password')
mysql_port = os.getenv('mysql_port')
# mysql engine
mysql_engine = create_engine(
    "mysql+pymysql://"+mysql_username+":"+mysql_password+"@localhost:"+mysql_port+"/"+mysql_db, echo=True)
# mysql session
mysqlSession = sessionmaker(bind=mysql_engine)
user = User(firstName='saket', lastName='kumar',
            email='saket.pes@gmail.com', phone='7259624334')
mysqlSession = mysqlSession()
dbAdd = mysqlSession.add(user)  # adding value in mysql table
mysqlSession.commit()

# postgresql credentails
postgresql_db = os.getenv('postgresql_db')
postgresql_username = os.getenv('postgresql_username')
postgresql_password = os.getenv('postgresql_password')
postgresql_port = os.getenv('postgresql_port')
# postgres connecting string
postgresql_engine = create_engine(
    'postgresql://'+postgresql_username+':'+postgresql_password+'@localhost:'+postgresql_port+'/'+postgresql_db)
# postgresql session
postgresqlSession = sessionmaker(bind=postgresql_engine)
book = Book(title='Rich Dad Poor Dad', author='Robert T. Kiyosaki',
            year='2017')
postgresqlSession = postgresqlSession()
postgresqlSession.add(book)  # adding value in postgres table
postgresqlSession.commit()

# API to fetch MySQL db data


@app.route('/MySQL')
def fetchDataMySQL():
    for row in mysqlSession.query(User).all():
        print(row)
    return "Mysql Data Fetched"

# API to fetch PostgreSQL db data


@app.route('/PostgreSQL')
def fetchDataPostgreSQL():
    for row in postgresqlSession.query(Book).all():
        print(row)
    return "PostgreSQL Data Fetched"
