# -*- coding: utf-8 -*-
"""
setup.py script
"""

import io
from collections import OrderedDict
from setuptools import setup
import os

with io.open("README.md", "rt", encoding="utf8") as f:
    README = f.read()


if os.environ.get("HISTORY_MODULE", None) == "history":
    setup(
        name="dojot.history",
        version="1.0.0",
        url="http://github.com/dojot/history",
        project_urls=OrderedDict((
            ("Code", "https://github.com/dojot/history.git"),
            ("Issue tracker", "https://github.com/dojot/history/issues"),
        )),
        license="GPL-3.0",
        author="Giovanni Curiel dos Santos",
        author_email="giovannicuriel@gmail.com",
        maintainer="dojot team",
        description="History retriever and manager",
        long_description=README,
        packages=["dojot.history"],
        include_package_data=True,
        zip_safe=False,
        platforms=[any],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            "falcon==1.0.0",
            "gunicorn==19.6.0",
            "gevent==1.1.1",
            "pymongo==3.2.2",
            "python-dateutil==2.7.5",
            "requests==2.20.0",
        ],
        extras_require={
            "dev": [
                "pytest==4.0.0",
                "pytest-cov==2.6.0"
            ]
        }
    )
elif os.environ.get("HISTORY_MODULE", None) == "persister":
    setup(
        name="dojot.persister",
        version="1.0.0",
        url="http://github.com/dojot/history",
        project_urls=OrderedDict((
            ("Code", "https://github.com/dojot/history.git"),
            ("Issue tracker", "https://github.com/dojot/history/issues"),
        )),
        license="GPL-3.0",
        author="Giovanni Curiel dos Santos",
        author_email="giovannicuriel@gmail.com",
        maintainer="dojot team",
        description="History retriever and manager",
        long_description=README,
        packages=["dojot.persister"],
        include_package_data=True,
        zip_safe=False,
        platforms=[any],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            "pymongo==3.2.2",
            "dojot.module==0.0.1a1",
            "python-dateutil==2.7.5"
        ],
        extras_require={
            "dev": [
                "pytest==4.0.0",
                "pytest-cov==2.6.0"
            ]
        }
    )