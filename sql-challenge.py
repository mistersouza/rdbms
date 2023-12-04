from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-base model fro the "Country" table


class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    continent = Column(String)
    population = Column(Integer)


# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Country table
brazil = Country(
    name="Brazil",
    continent="South America",
    population=200000000
)

# add instance of our country to our session
session.add(brazil)

# commit out session to the database
session.commit()

country = session.query(Country).first()
print(
    country
)
