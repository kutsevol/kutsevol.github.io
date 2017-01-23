#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Artur Kutsevol'
SITENAME = 'Artur Kutsevol Blog'
SITEURL = ''


PATH = 'content'
ARTICLE_PATHS = ['articles',]
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_PATHS = ['pages',]
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/kutsevol'),
          ('Linkedin', 'https://www.linkedin.com/in/arthur-kutsevol-a20731a4'),)

DEFAULT_PAGINATION = 10
THEME =  "themes/elegant"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
