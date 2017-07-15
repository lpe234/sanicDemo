# -*- coding: UTF-8 -*-

from sanic import Blueprint
from sanic.response import json

__author__ = 'lpe234'

"""
version 2 api
"""

bp_v2 = Blueprint('bp_v2')


@bp_v2.get('/')
async def default(request):
    """
    default demo api
    :param request:
    :return:
    """
    return json({
        'version': 'v2'
    })
