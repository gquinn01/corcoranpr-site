/* ==============================================================
   CORCORAN COMMUNICATIONS, shared behavior for every page.
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

/* ---------- audit request form ----------
   Progressive enhancement. With this script off the form posts normally
   to Formspree and the browser navigates to their confirmation, which is
   why the form keeps a real action and method in the markup. With it on
   we post in the background and swap the thank you in place, so nobody
   loses the page they were reading.
   Field validation is left to the browser: the inputs carry required and
   the right types, so an invalid form never reaches this handler and the
   native messages do the work in the user's own language. */
(function () {
  var form = document.querySelector('.audit-form');
  if (!form || !window.fetch) return;
  var thanks = document.querySelector('.af-thanks');
  var errBox = form.querySelector('.af-error');
  var button = form.querySelector('.af-submit');

  function fail(msg) {
    errBox.innerHTML = msg;
    errBox.hidden = false;
    button.disabled = false;
    button.textContent = 'Send My Free Audit';
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    errBox.hidden = true;
    button.disabled = true;
    button.textContent = 'Sending...';

    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    }).then(function (res) {
      if (!res.ok) throw new Error('bad status');
      form.hidden = true;
      thanks.hidden = false;
      thanks.focus && thanks.focus();

      /* Conversion signal. Pushed to the dataLayer and to gtag if either
         is present, and also dispatched as a DOM event so anything else
         can listen without us knowing about it in advance.
         CONVERSION TAG: at domain cutover, put the Google Ads conversion
         snippet for this action right here. */
      var detail = { form: 'audit-request' };
      if (window.dataLayer) window.dataLayer.push({ event: 'form_submit', form: 'audit-request' });
      if (typeof window.gtag === 'function') window.gtag('event', 'form_submit', detail);
      document.dispatchEvent(new CustomEvent('form_submit', { detail: detail }));
    }).catch(function () {
      fail('That did not send. Email <a href="mailto:greg@corcoranpr.com">greg@corcoranpr.com</a> ' +
           'and we will pick it up from there, or call or text 215-259-8304.');
    });
  });
})();
