# -*- coding: UTF-8 -*-

from sanic import Blueprint
from sanic.response import json

from model.user import User


__author__ = 'lpe234'


"""
version 1 api
"""

bp_v1 = Blueprint('bp_v1')


@bp_v1.get('/')
async def default(request):
    """
    default demo api
    :param request:
    :return:
    """
    return json({
        'version': 'v1'
    })


@bp_v1.get('/users')
async def users(request):
    return json({
        'users': User.select()
    })


@bp_v1.post('/users')
async def users(request):
    # TODO: Parameters check
    user = User(**request.json)
    # TODO: Service && Transaction
    user.save()
    return json({
        'user': user
    })


@bp_v1.get('/users/<uid:int>')
async def user(request, uid):
    user = User.get(User.id == uid)
    return json({
        'user': user
    })


@bp_v1.delete('/users/<uid:int>')
async def user(request, uid):
    user = User.get(User.id == uid)
    user.delete_instance()
    return json({

    })


@bp_v1.put('/users/<uid:int>')
async def user(request, uid):
    # TODO: UPDATE USER
    return json({})
