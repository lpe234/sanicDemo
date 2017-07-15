# -*- coding: UTF-8 -*-
import socket

from sanic import Sanic
from sanic.response import json

import settings

from api_v1 import bp_v1
from api_v2 import bp_v2

__author__ = 'lpe234'


app = Sanic()

# load config by hostname, and check config.
host_name = socket.gethostname().capitalize().replace('.', '_').replace('-', '')
app.config.from_object(getattr(settings, '{}sConfig'.format(host_name), settings.Config))
if app.config.get('CONFIG_NAME'):
    # FIXME: use log
    print('load config from: {}'.format(app.config.get('CONFIG_NAME')))
else:
    # FIXME: use log
    print('config may be wrong, please check with host_name: {}'.format(host_name))
    exit()

# register blueprints on the app
app.blueprint(bp_v1, url_prefix='/v1')
app.blueprint(bp_v2, url_prefix='/v2')


@app.get('/')
async def test(request):
    return json({
        'hello': 'world'
    })


if __name__ == '__main__':
    app.run()

