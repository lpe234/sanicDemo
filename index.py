# -*- coding: UTF-8 -*-

from sanic import Sanic
from sanic.response import json

__author__ = 'lpe234'


app = Sanic()


@app.route('/')
async def test(request):
    return json({
        'hello': 'world'
    })

if __name__ == '__main__':
    app.run()

