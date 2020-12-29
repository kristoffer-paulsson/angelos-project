#!/usr/bin/env python
#
# Copyright (c) 2020 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
#
# This material may be distributed only subject to the terms and conditions set
# forth in the Open Publication License, v1.0 or later (the latest version is
# presently available at http://www.opencontent.org/openpub/).
#
# Distribution of substantively modified versions of this document is prohibited
# without the explicit permission of the copyright holder.
#
# Authors:
#     Kristoffer Paulsson - initial author
#

from setuptools import setup

config = {
    "name": "angelos-doc",
    "version": "1.0",
    "license": "Open Publication License",
    "description": "Website repository for the Angelos project",
    "author": "Kristoffer Paulsson",
    "author_email": "kristoffer.paulsson@talenten.se",
    "classifiers": [
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: Free To Use But Restricted",
        "Topic :: Documentation"
    ],
    "install_requires": ["pelican", "markdown"]
}

setup(**config)