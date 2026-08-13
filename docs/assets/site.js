/* ==============================================================
   CORCORAN COMMUNICATIONS, shared behaviour for every page.
   Loaded with `defer` so it never blocks rendering.

   Contents: the mobile navigation menu, and nothing else. The hero
   dashboard animation is homepage-only and stays inline there.
   ============================================================== */
(function () {
  var toggle = document.querySelector('.navtoggle');
  var menu = document.getElementById('navmenu');
  if (!toggle || !menu) return;

  function setOpen(open) {
    menu.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  toggle.addEventListener('click', function () {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  // Tapping a link navigates or jumps to an anchor on this page. Either
  // way the panel should not stay open over the destination.
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  // Above 1000px the links are back in the bar and the panel styles no
  // longer apply, so an open panel would leave aria-expanded lying.
  window.addEventListener('resize', function () {
    if (window.innerWidth > 1000) setOpen(false);
  });
})();
