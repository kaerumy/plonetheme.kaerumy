=================
Theme Development
=================

This is a Diazo theme for Plone 6, based on the "Clean Blog" theme by
`Start Bootstrap <https://startbootstrap.com/template/clean-blog>`_
(see ``LICENSE`` for the asset license).

Layout
======

- ``index.html``   the theme HTML template (Bootstrap 3 markup)
- ``rules.xml``    the Diazo transformation rules (Plone 6 Classic UI selectors)
- ``manifest.cfg`` the theme manifest (prefix, production css, parameters)
- ``css/``         ``bootstrap.min.css``, ``main.css`` (from Clean Blog) and
  ``plone6.css`` (compatibility styles for Plone 6 markup differences)
- ``fonts/``       glyphicons fonts used by bootstrap.min.css
- ``img/``         ``home-bg.jpg`` used as the intro header background
- ``js/``          ``clean-blog.min.js`` (from Clean Blog, needs the jQuery
  that ships in the Plone 6 ``plone`` resource bundle) and ``theme.js``
  (vanilla-JS mobile navbar toggle for the Bootstrap 3 markup)
- ``tinymce-templates/``  Bootstrap page templates for TinyMCE

Development
===========

The theme files are plain static assets, there is no build step.

1. Install the add-on in a Plone 6 site (control panel > Add-ons, or
   ``plonecli``/buildout depending on your setup).
2. Enable the theme in the control panel > Site > Theming.
3. Edit ``index.html`` / ``rules.xml`` / the CSS and reload the page.
   No compilation is required.

Diazo debug output
------------------

Append ``?diazo`` to a URL to inspect the transformed output
(enable "Debug mode" in the Theming control panel first).
