
best-browsable-api for Django Rest Framework
############################################

.. image:: https://img.shields.io/travis/Nekmo/best-browsable-api.svg?style=flat-square&maxAge=2592000
  :target: https://travis-ci.org/Nekmo/best-browsable-api
  :alt: Latest Travis CI build status

.. image:: https://img.shields.io/pypi/v/best-browsable-api.svg?style=flat-square
  :target: https://pypi.org/project/best-browsable-api/
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/best-browsable-api.svg?style=flat-square
  :target: https://pypi.org/project/best-browsable-api/
  :alt: Python versions

.. image:: https://img.shields.io/codeclimate/github/Nekmo/best-browsable-api.svg?style=flat-square
  :target: https://codeclimate.com/github/Nekmo/best-browsable-api
  :alt: Code Climate

.. image:: https://img.shields.io/codecov/c/github/Nekmo/best-browsable-api/master.svg?style=flat-square
  :target: https://codecov.io/github/Nekmo/best-browsable-api
  :alt: Test coverage

.. image:: https://img.shields.io/requires/github/Nekmo/best-browsable-api.svg?style=flat-square
     :target: https://requires.io/github/Nekmo/best-browsable-api/requirements/?branch=master
     :alt: Requirements Status

To install Best Browsable API, run this command in your django project:

.. code-block:: console

    $ pip install -e git+https://github.com/Nekmo/best-browsable-api.git@master#egg=best_browsable_api

And add ``best_browsable_api`` to your ``INSTALLED_APPS`` setting (before ``rest_framework``):

.. code-block:: python

    INSTALLED_APPS = [
        "best_browsable_api",  # Before rest_framework!
        "rest_framework",
    ]


Collapse tree
=============
Is your json too big? The library collapses the browsable api tree.

.. image:: https://raw.githubusercontent.com/Nekmo/best-browsable-api/master/images/collapse_tree.png
    :width: 200px
    :align: right

