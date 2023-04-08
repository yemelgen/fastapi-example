#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from configparser import ConfigParser
from os.path import dirname, abspath

config = ConfigParser()
WORKDIR = dirname( dirname( abspath( __file__ ) ) )
config.read('settings.ini')
DATABASE_URI = config.get('database', 'uri', fallback='sqlite://test.db').strip('"')
LOGFILE = config.get('logging', 'file', fallback='debug.log').strip('"')
