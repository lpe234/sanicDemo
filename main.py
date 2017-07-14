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

# sample rest api
all_tags = [
    'red',
    'green',
    'blue'
]


@app.route('/tags', methods=['GET'])
async def tags(request):
    return json(all_tags)


@app.route('/tags/<tid:int>', methods=['GET'])
async def tag(request, tid):
    return json(all_tags[tid])


@app.route('/tags/<tid:int>', methods=['DELETE'])
async def tag(request, tid):
    del all_tags[tid]
    return json(all_tags)


if __name__ == '__main__':
    app.run()

