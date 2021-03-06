#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '张本轩'
SITENAME = 'Stupidfish'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-themes/svbtle'

# Blogroll
LINKS = (('Github', 'https://github.com/sjtuzbx'),
        ('Blogger', 'https://stupidbookfish.blogspot.com/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# math
PLUGIN_PATHS=['pelican-plugins']
PLUGINS = ["render_math"]

## load cache
LOAD_CONTENT_CACHE = False

## typogrify
TYPOGRIFY = True

SUMMARY_MAX_LENGTH = 30

