# -*- coding: UTF-8 -*-

__author__ = 'lpe234'


"""
config module
"""


class Config(object):
    """
    basic config
    """
    CONFIG_NAME = None
    DEBUG = False
    LOGO = """
   _____             _      _____                       
  / ____|           (_)    |  __ \                      
 | (___   __ _ _ __  _  ___| |  | | ___ _ __ ___   ___  
  \___ \ / _` | '_ \| |/ __| |  | |/ _ \ '_ ` _ \ / _ \ 
  ____) | (_| | | | | | (__| |__| |  __/ | | | | | (_) |
 |_____/ \__,_|_| |_|_|\___|_____/ \___|_| |_| |_|\___/     
"""


class ProductConfig(Config):
    """
    product config
    """
    pass


class DevelopConfig(Config):
    """
    develop config
    """
    DEBUG = True


class Lupengdemacbookpro_localConfig(DevelopConfig):
    """
    self config
    """
    CONFIG_NAME = 'LupengConfig'
    pass


class BogonConfig(Lupengdemacbookpro_localConfig):
    """
    Bogon Fix
    """
    pass
