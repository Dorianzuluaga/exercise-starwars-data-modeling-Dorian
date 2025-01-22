import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    email = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)

class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    manufacturer = Column(String(250))
    class_nave = Column(String(250))
    cost = Column(String(250))
    speed = Column(String(250))
    length = Column(Integer)
    cargo_capaciti = Column(String(250))
    minimum_crew = Column(Integer)
    passengers = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    naves_id = Column(Integer, ForeignKey('naves.id'))
    naves = relationship(Naves)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
