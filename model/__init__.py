# -*- coding: UTF-8 -*-

from peewee import SqliteDatabase
from peewee import Model


__author__ = 'lpe234'


db = SqliteDatabase('sanicDemo.db')


class BaseModel(Model):
    """
    Base Model
    """
    class Meta:
        database = db


def create_tables():
    """
    create table
    :return:
    """
    from model.user import User
    db.connect()
    db.create_tables([User, ])
    db.commit()
