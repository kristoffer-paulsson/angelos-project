#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kristoffer Paulsson'
SITENAME = 'The Angelos Project'
SITEURL = 'https://angelos-project.com'

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Angelos repo', 'https://github.com/kristoffer-paulsson/angelos'),
    ('Logo Messenger repo', 'https://github.com/kristoffer-paulsson/logo'),
)

# Social widget
# SOCIAL = (("", ""),)

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/bootstrap2"