#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Artur Kutsevol'
SITENAME = 'Artur Kutsevol Blog'
SITEURL = ''

PATH = 'content'

ARTICLE_PATHS = ('articles',)
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = ('pages',)
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

STATIC_PATHS = ('images', 'extra/favicon.ico')
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://github.com/kutsevol'),
          ('Linkedin', 'https://www.linkedin.com/in/arthur-kutsevol-a20731a4'),)

DEFAULT_PAGINATION = 10
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

MENUITEMS = (('Home', '/'),
            ('About', '/about-me/index.html'))
THEME =  "themes/elegant"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
