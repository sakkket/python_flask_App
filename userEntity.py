from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return "<User(firstName='%s', lastName='%s', email='%s', phone='%s' )>" % (self.firstName, self.lastName, self.email, self.phone)


class Book(Base):
    __tablename__ = 'books'
    title = Column(String, primary_key=True)
    author = Column(String)
    year = Column(String)

    def __repr__(self):
        return "<Books(title='%s', author='%s', year='%s' )>" % (self.title, self.author, self.year)
