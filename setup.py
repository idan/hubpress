# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

import hubpress


setup(
    name='hubpress',
    version=hubpress.__version__,
    author='Idan Gazit',
    author_email='idan@gazit.me',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/idangazit/hubpress',
    license='BSD licence, see LICENSE file',
    description='Github-driven Django blog app',
    long_description=open('README.md').read(),
    install_requires=[
        'Django',
        'django-taggit',
        'requests>=0.8.3',
        'Markdown>=2.1.0',
        'smartypants>=1.6.0.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
#    test_suite='runtests.runtests',
    zip_safe=False,
)