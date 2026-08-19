/* ==============================================================
   CORCORAN COMMUNICATIONS, shared behavior for every page.
   Loaded with `defer` so it never blocks rendering.

   Contents: the mobile navigation menu, the audit request form, and
   the stat band count-up. The hero dashboard animation is homepage-only
   and stays inline there.
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

/* ---------- stat band count-up ----------
   The real numbers live in the HTML as text, so the audit, a crawler and
   a reader with JavaScript off all see 98%, 908% and 26 years. Nothing
   here is the source of those values. This reads whatever the markup
   already says, drops it to zero, and counts back up to the same number
   the first time the band scrolls into view.

   Parsed rather than hardcoded for the same reason: if the numbers in
   the markup are ever corrected, the animation follows them instead of
   counting up to a stale figure the script remembers.

   Only the digits animate. The suffix is whatever followed them, so
   "%" and " years" are carried through untouched on every frame.

   The homepage hero gauge does the same thing with its own inline
   script and is deliberately left alone. */
(function () {
  var bands = document.querySelectorAll('.statgrid');
  if (!bands.length) return;

  /* No animation at all under reduced motion. Returning here leaves the
     markup exactly as it shipped, which IS the final value, so there is
     nothing to restore. */
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  function collect(band) {
    var nodes = band.querySelectorAll('.stat b');
    var items = [];
    for (var i = 0; i < nodes.length; i++) {
      var m = /^(\d[\d,]*)(.*)$/.exec(nodes[i].textContent.trim());
      if (!m) continue;   // not a number we can count, so leave it alone
      items.push({
        el: nodes[i],
        to: parseInt(m[1].replace(/,/g, ''), 10),
        suffix: m[2]
      });
      nodes[i].textContent = '0' + m[2];
    }
    return items;
  }

  /* Cubic ease-out, the same curve as the homepage gauge, so the two
     decelerate alike. p reaches exactly 1, so the last frame always
     writes the true number rather than a rounded near miss. */
  function run(items) {
    var t0 = null;
    requestAnimationFrame(function step(t) {
      if (t0 === null) t0 = t;
      var p = Math.min(1, (t - t0) / 1100);
      var eased = 1 - Math.pow(1 - p, 3);
      for (var i = 0; i < items.length; i++) {
        items[i].el.textContent = Math.round(items[i].to * eased) + items[i].suffix;
      }
      if (p < 1) requestAnimationFrame(step);
    });
  }

  for (var b = 0; b < bands.length; b++) {
    (function (band) {
      var items = collect(band);
      if (!items.length) return;

      // No observer, no trigger to wait for: just show the count.
      if (!('IntersectionObserver' in window)) { run(items); return; }

      var io = new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            run(items);
            io.disconnect();   // once per page load, never again
            return;
          }
        }
      }, { threshold: .3 });
      io.observe(band);
    })(bands[b]);
  }
})();
