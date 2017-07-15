# -*- coding: UTF-8 -*-

import unittest

from main import app

__author__ = 'lpe234'


"""
test module
"""


class Test(unittest.TestCase):
    """
    unittest
    """

    def test_index_returns_200(self):
        """
        test index return 200
        :return:
        """
        request, response = app.test_client.get('/')
        assert response.status == 200

