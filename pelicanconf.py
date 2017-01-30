#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Artur Kutsevol'
SITENAME = 'Artur Kutsevol'
# SITEURL = 'https://kutsevol.github.io'
SITEURL = 'http://localhost:8000'

# Regional Settings
TIMEZONE = 'Europe/Kiev'
DEFAULT_LANG = 'ru'

# Appearance
THEME = "themes/elegant"
DEFAULT_PAGINATION = False
DISQUS_SITENAME = 'https-kutsevol-github-io'
DISQUS_SECRET_KEY = '9FZCEd68QqB922yIpekhEdGPuYyDtHHL7QDWEWAn7ksqqG9wGbCEGpi3Xmlwvz1S'
DISQUS_PUBLIC_KEY = 'uSBTrCKfTVPFtmuidGHlorzxOPPSfGcm2ab7Hxisfpa8zXcWI3iJLjLiLVnNMJyL'

# Paths and urls
PATH = 'content'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['disqus_static']

ARTICLE_PATHS = ('articles',)
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = ('pages',)
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

STATIC_PATHS = ('images', 'extra/favicon.ico')
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

MENUITEMS = (('About', '/about/index.html'),)
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://github.com/kutsevol'),
          ('Linkedin', 'https://www.linkedin.com/in/arthur-kutsevol-a20731a4'),
          )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
