Changelog
=========


1.0a1 (unreleased)
------------------

- Complete the port of the P5 site's custom.css in css/plone6.css: hide
  the latest-note collection heading (not just the byline) for anonymous
  visitors, and apply the P5 item title (sohne stack, 48px, no
  underline) and item description (sohne stack, 22px, grey) styling to
  the Plone 6 full-view markup (h1 > a.summary.url, .item p.lead).
  [kaerumy]

- Fix TinyMCE "Insert image" (and link) dialog: the theme's Bootstrap 3
  (`.fade { opacity: 0 }`, `.modal.fade .modal-dialog` transform/margins)
  overrode the Bootstrap 5 rules of Plone 6's plone-modal pattern, so the
  dialog was invisible or mispositioned. Re-assert the Bootstrap 5
  behaviour in css/plone6.css.
  [kaerumy]

- Keep Plone 6 modals within the viewport (`.modal-dialog` max-height,
  scrolling `.modal-body`) and compact the TinyMCE image dialog's
  selected-items list (auto-width chips, 40px thumbnail, single-line
  title, no path), which previously grew taller than the dialog.
  [kaerumy]

- Fix the theme manifest's ``tinymce-content-css`` value: it lacked the
  leading slash (barceloneta uses ``/++theme++...``), so CMFPlone's URL
  concatenation produced ``{portal}++theme++.../css/main.css`` (missing
  slash) and the TinyMCE content iframe got a 404 instead of the theme
  CSS.
  [kaerumy]

- Remove the ``plone.custom_plugins`` TinyMCE registry record, which
  registered the ``template`` plugin from the Plone 5 static path
  (``++plone++static/components/tinymce-builded/...``). That path no
  longer exists in Plone 6 (plugins are pre-bundled in
  plone.staticresources), so every editor load produced a 404 console
  error. Note: the template plugin is not part of the Plone 6 bundle,
  so the ``plone.templates`` list has no effect on Plone 6 either.
  [kaerumy]

- Initial release.
  [kaerumy]
