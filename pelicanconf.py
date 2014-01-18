#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Benoit Dherin & Jarrod Millman'
SITENAME = u"UC Berkeley's Statistics 133"
SITESUBTITLE = u'Concepts in Computing with Data (Spring 2014)'
SITEURL = '' # change in publishconf.py

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/berkeley-stat133'),
          ('Piazza', 'https://piazza.com/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.join(os.environ.get('HOME'),
                     'src/pelican/pelican-bootstrap3/')
PLUGIN_PATH = os.path.join(os.environ.get('HOME'),
                           'src/pelican/pelican-plugins')
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']
