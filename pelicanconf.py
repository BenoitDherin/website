#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Jarrod Millman'
SITENAME = u"UC Berkeley's Statistics 133"
SITESUBTITLE = u'Concepts in Computing with Data (Spring 2014)'
SITEURL = '' # change in publishconf.py

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

## Title menu options (this isn't necessary, but I wanted to have more control)
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
#MENUITEMS = [('Course Information', 'http://berkeley-stat133.github.io/pages/info.html'),
#             ('Syllabus', 'http://berkeley-stat133.github.io/pages/syllabus.html'),
#             ('Lectures', 'http://berkeley-stat133.github.io/pages/lectures.html'),
#             ('Labs', 'http://berkeley-stat133.github.io/pages/labs.html'),
#             ('Cloud', 'http://berkeley-stat133.github.io/pages/cloud.html'),
#             ('Assignments', 'http://berkeley-stat133.github.io/pages/assignments.html'),]

# Blogroll
LINKS =  (('Course website', 'http://nbviewer.ipython.org/urls/db.tt/IPY60OHY?create=1'),
          ('Software Carpentry', 'http://software-carpentry.org'),)
# Social widget
SOCIAL = (('Github', 'https://github.com/berkeley-stat133'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/'
PLUGIN_PATH = os.path.join(os.environ.get('HOME'),
                           'src/pelican/pelican-plugins')
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

STATIC_PATHS = ['notebooks']

# The theme file should be updated so that the base header contains the line:
#
# {% if EXTRA_HEADER %}
# {{ EXTRA_HEADER }}
# {% endif %}
#
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

CC_LICENSE = "CC-BY-NC-SA"
