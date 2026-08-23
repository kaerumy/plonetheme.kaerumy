/*
  plonetheme.kaerumy
  Plone 6 compatibility: Bootstrap 3 style mobile navbar toggle.

  Plone 6 ships Bootstrap 5 (no jQuery collapse plugin for the Bootstrap 3
  markup of this theme), so the theme's own toggle is driven here.
*/
(function () {
  "use strict";

  function init() {
    var toggle = document.querySelector(".navbar-toggle");
    var collapse = document.getElementById("bs-example-navbar-collapse-1");
    if (!toggle || !collapse) {
      return;
    }

    function setOpen(open) {
      if (open) {
        collapse.classList.add("in");
      } else {
        collapse.classList.remove("in");
      }
      if (!open) {
        toggle.classList.add("collapsed");
      } else {
        toggle.classList.remove("collapsed");
      }
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    }

    toggle.addEventListener("click", function () {
      setOpen(!collapse.classList.contains("in"));
    });

    // Close the menu after picking a navigation link (mobile behaviour)
    collapse.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        setOpen(false);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
