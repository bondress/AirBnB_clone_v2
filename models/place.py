#!/usr/bin/python3
"""Place Module for AirBnB project"""

from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place',
                           cascade='all, delete, delete-orphan')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False)

    @property
    def review(self):
        ''' returns list of review instances with place_id
        equals to the current Place.id
        FileStorage relationship between Place and Review
        '''
        all_revs = []
        for r in list(models.storage.all(Review).values()):
            if r.place_id == self.id:
                all_revs.append(r)
        return all_revs

    @property
    def amenities(self):
        ''' returns the list of Amenity instances
        based on the attribute amenity_ids that
        contains all Amenity.id linked to the Place
        '''
        all_amens = []
        for a in list(models.storage.all(Amenity).values()):
            if a.id in self.amenity_ids:
                all_amens.append(a)
        return all_amens

    @amenities.setter
    def amenities(self, obj):
        ''' method for adding an Amenity.id to the
        attribute amenity_ids. accepts only Amenity
        objects
        '''
        if obj is not None:
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
