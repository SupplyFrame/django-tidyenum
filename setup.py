# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import tidyenum

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = tidyenum.__version__

requires = []
if sys.version[:2] < (3, 4):
    requires.append('enum34')

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-tidyenum',
    version=version,
    description='Django choices fields driven by PEP435 Enums.',
    long_description=readme + '\n\n' + history,
    author='Christopher Lambacher',
    author_email='chris@kateandchris.net',
    url='https://github.com/tindie/django-tidyenum',
    packages=[
        'tidyenum',
    ],
    include_package_data=True,
    install_requires=requires,
    license="BSD",
    zip_safe=False,
    keywords='django-tidyenum',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
