#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Artur Kutsevol'
SITENAME = 'Artur Kutsevol Blog'
SITEURL = 'https://kutsevol.github.io'

PATH = 'content'
OUTPUT_PATH = "."
OUTPUT_SOURCES = True

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
GITHUB_URL = "https://github.com/kutsevol"
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/kutsevol'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
THEME =  "themes/elegant"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
