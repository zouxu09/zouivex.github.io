#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'九哥'
SITENAME = u'九哥的部落'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'zh'
HTML_LANG = u'zh'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/zouivex'),
          ('linkedin', 'https://cn.linkedin.com/in/zouivex'),
          ('google plus', 'https://plus.google.com/u/0/104327320364152471669/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'pdf',
    'extra/CNAME'
    ]

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Same as Octopress structure
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Extract metadata from file name
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Use totally new generated files each time
DELETE_OUTPUT_DIRECTORY = True

# Make blog more beautiful
TYPOGRIFY = True

# This is a single author site
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

#Theme configurations: foundation-default-colours
THEME = 'theme/pelican-simplegrey'

# Plugins
#PLUGIN_PATHS = ["plugins"]
#PLUGINS = ["assets", "liquid_tags", "sitemap"]

DISQUS_SITENAME = 'httpzouivexgithubio'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Support PDF download
# PDF_PROCESSOR = True

# Count of different font sizes in the tag cloud.
TAG_CLOUD_STEPS = 4

# Maximum number of tags in the cloud.
TAG_CLOUD_MAX_ITEMS = 100

# Feed configuration
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
