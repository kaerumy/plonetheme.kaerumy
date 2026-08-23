.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/plonetheme.kaerumy/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/plonetheme.kaerumy/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/plonetheme.kaerumy/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/plonetheme.kaerumy?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/plonetheme.kaerumy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/plonetheme.kaerumy

.. image:: https://img.shields.io/pypi/v/plonetheme.kaerumy.svg
    :target: https://pypi.python.org/pypi/plonetheme.kaerumy/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/plonetheme.kaerumy.svg
    :target: https://pypi.python.org/pypi/plonetheme.kaerumy
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/plonetheme.kaerumy.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/plonetheme.kaerumy.svg
    :target: https://pypi.python.org/pypi/plonetheme.kaerumy/
    :alt: License


==================
plonetheme.kaerumy
==================

A Diazo based Plone 6 theme (Clean Blog) for kaerumy

Features
--------

- "Clean Blog" look (by `Start Bootstrap <https://startbootstrap.com/template/clean-blog>`_)
  ported from a Plone 5 theme to the Plone 6 Classic UI.
- Diazo ``rules.xml`` targeting the Plone 6 (Mockup) page structure: edit bar,
  portal navigation (``#portal-globalnav``), searchbox, logo, breadcrumbs,
  portlet columns and footer.
- Bootstrap 3 based styling (``bootstrap.min.css`` + ``main.css``) plus a small
  ``plone6.css`` that compensates for markup differences in Plone 6.
- Login / member tools and site title injected into the intro header.
- Vanilla-JS mobile navbar toggle (``js/theme.js``) so the responsive menu
  works without the Bootstrap 3 jQuery collapse plugin.
- TinyMCE Bootstrap page templates.

Examples
--------

- This theme is used on the kaerumy Plone sites.


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install plonetheme.kaerumy by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plonetheme.kaerumy


and then running ``bin/buildout``


Authors
-------

Provided by awesome people ;)


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/plonetheme.kaerumy/issues
- Source Code: https://github.com/collective/plonetheme.kaerumy
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
