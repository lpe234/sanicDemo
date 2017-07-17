# -*- coding: UTF-8 -*-

from peewee import CharField, DateField, BooleanField, IntegerField

from model import BaseModel

__author__ = 'lpe234'


class User(BaseModel):
    """
    User model
    """
    id = IntegerField(primary_key=True)
    name = CharField(max_length=32)
    age = IntegerField()
    birthday = DateField(formats='%Y-%m-%d %H:%M:%S')
    is_relative = BooleanField()
