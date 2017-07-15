# -*- coding: UTF-8 -*-

from sanic import Blueprint
from sanic.response import json

__author__ = 'lpe234'

"""
version 1 api
"""

bp_v1 = Blueprint('bp_v1')


@bp_v1.route('/', methods=['GET'])
async def default(request):
    """
    default demo api
    :param request:
    :return:
    """
    return json({
        'version': 'v1'
    })
