# -*- coding: UTF-8 -*-

from sanic import Sanic
from sanic.response import json

from api_v1 import bp_v1
from api_v2 import bp_v2

__author__ = 'lpe234'


app = Sanic()

# register blueprints on the app
app.blueprint(bp_v1, url_prefix='/v1')
app.blueprint(bp_v2, url_prefix='/v1')


@app.get('/')
async def test(request):
    return json({
        'hello': 'world'
    })


if __name__ == '__main__':
    app.run()

