#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Kristoffer Paulsson"
SITEURL = "https://angelos-project.com"
SITENAME = "The Angelos Project"
SITETITLE = SITENAME
SITESUBTITLE = "Ἄγγελος: messenger of divine message, Λόγῳ: word with an intent."
SITEDESCRIPTION = ""
SITELOGO = SITEURL + "/images/angelos.png"
FAVICON = SITEURL + "/images/favicon.ico"

PATH = "content"
TIMEZONE = "Europe/Stockholm"
ROBOTS = "index, follow"
I18N_TEMPLATES_LANG = DEFAULT_LANG = "en"
COPYRIGHT_YEAR = "2020-2021"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# SOCIAL = (("", ""),)

ARTICLE_ORDER_BY = 'sort'
PAGE_ORDER_BY = 'order'

CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme/flex"
STATIC_PATHS = ["images"]

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MAIN_MENU = False
MENU_ITEMS= [
    ("Home", "index.html"),
    # ("About", "about.html"),
    ("Users", "/user.html"),
    ("Administratos", "/administrator.html"),
    ("Developers", "/developer.html"),
]

LINKS = (

)