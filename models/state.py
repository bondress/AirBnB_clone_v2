#!/usr/bin/python3
"""This modulce contains class State
(0x04 update)"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State Class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="states")

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns City instances"""
            city_vals = models.storage.all("City").values()
            all_cities = []
            for city in city_vals:
                if city.state_id == self.id:
                    all_cities.append(city)
            return all_cities
