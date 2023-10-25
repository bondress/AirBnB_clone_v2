#!/usr/bin/python3
<<<<<<< HEAD
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
=======
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlachemy import Column, String
from models import storage_type
>>>>>>> 7caf28ff500a1e9b848553ea807079ad29041485
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
=======
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    if storage_type == 'db':
>>>>>>> 7caf28ff500a1e9b848553ea807079ad29041485
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
=======
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
>>>>>>> 7caf28ff500a1e9b848553ea807079ad29041485
