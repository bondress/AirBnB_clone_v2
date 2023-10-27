#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if getenv("HBNB_TYPE_STORAGE", None) is None:
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            all_cities = []
            for c in list(models.storage.all(City).values()):
                if c.state_id == self.id:
                    all_cities.append(c)
            return all_cities
