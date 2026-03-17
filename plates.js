fetch("http://127.0.0.1:8000/menu")

(function(){
  // ── Inline Manifest via Blob ─────────────────────────────────────
  const manifest = {
    name: "Uncle Moro Varadero Food Truck",
    short_name: "Uncle Moro",
    description: "Authentic Cuban & Street Food at Saskatchewan Powwows",
    start_url: "./uncle_moro_menu_en.html",
    display: "standalone",
    background_color: "#003d6b",
    theme_color: "#0096c7",
    orientation: "portrait-primary",
    icons: [
      { src: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 192 192'><rect width='192' height='192' rx='32' fill='%230096c7'/><text y='.85em' font-size='140' x='20'>🌮</text></svg>", sizes: "192x192", type: "image/svg+xml" },
      { src: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'><rect width='512' height='512' rx='80' fill='%230096c7'/><text y='.85em' font-size='380' x='50'>🌮</text></svg>", sizes: "512x512", type: "image/svg+xml", purpose: "any maskable" }
    ],
    screenshots: [],
    categories: ["food", "lifestyle"]
  };
  const blob = new Blob([JSON.stringify(manifest)], {type:'application/manifest+json'});
  const url = URL.createObjectURL(blob);
  const link = document.createElement('link');
  link.rel = 'manifest'; link.href = url;
  document.head.appendChild(link);

  // ── Inline Service Worker via Blob ───────────────────────────────
  const swCode = `
    const CACHE = 'uncle-moro-v1';
    const ASSETS = [location.href];
    self.addEventListener('install', e => {
      e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
      self.skipWaiting();
    });
    self.addEventListener('activate', e => {
      e.waitUntil(caches.keys().then(keys => Promise.all(
        keys.filter(k => k !== CACHE).map(k => caches.delete(k))
      )));
      self.clients.claim();
    });
    self.addEventListener('fetch', e => {
      e.respondWith(
        caches.match(e.request).then(cached => cached || fetch(e.request).catch(() => cached))
      );
    });
  `;
  if ('serviceWorker' in navigator) {
    const swBlob = new Blob([swCode], {type:'text/javascript'});
    const swUrl = URL.createObjectURL(swBlob);
    navigator.serviceWorker.register(swUrl, {scope: './'}).catch(()=>{});
  }

  // ── Install Banner ───────────────────────────────────────────────
  let deferredPrompt = null;
  window.addEventListener('beforeinstallprompt', e => {
    e.preventDefault();
    deferredPrompt = e;
    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'flex';
  });
  window.addEventListener('appinstalled', () => {
    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'none';
  });
  window._installPWA = function() {
    if (deferredPrompt) { deferredPrompt.prompt(); deferredPrompt = null; }
    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'none';
  };
  window._dismissBanner = function() {
    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'none';
  };
})();


let current = 0;
const total = 5;
const pages = document.getElementById('pages');
const dots = document.querySelectorAll('.dot');
const topbar = document.getElementById('topbar');
let startX = 0;
let dragging = false;

function goTo(n) {
  current = Math.max(0, Math.min(total - 1, n));
  pages.style.transform = 'translateX(-' + (current * 20) + '%)';
  dots.forEach((d, i) => d.classList.toggle('active', i === current));
  // Re-trigger hero animations
  const activePage = pages.querySelectorAll('.page')[current];
  const els = activePage.querySelectorAll('.hero-category, .hero-name, .hero-price-row');
  els.forEach(el => { el.style.animation = 'none'; el.offsetHeight; el.style.animation = ''; });
}

// Touch/swipe
pages.addEventListener('touchstart', e => { startX = e.touches[0].clientX; dragging = true; }, {passive:true});
pages.addEventListener('touchend', e => {
  if (!dragging) return;
  const diff = startX - e.changedTouches[0].clientX;
  if (Math.abs(diff) > 50) diff > 0 ? goTo(current + 1) : goTo(current - 1);
  dragging = false;
});

// Mouse swipe desktop
pages.addEventListener('mousedown', e => { startX = e.clientX; dragging = true; });
window.addEventListener('mouseup', e => {
  if (!dragging) return;
  const diff = startX - e.clientX;
  if (Math.abs(diff) > 60) diff > 0 ? goTo(current + 1) : goTo(current - 1);
  dragging = false;
});

// Scroll topbar
window.addEventListener('scroll', () => {
  topbar.classList.toggle('solid', window.scrollY > 80);
}, {passive:true});

// Keyboard nav
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight') goTo(current + 1);
  if (e.key === 'ArrowLeft') goTo(current - 1);
});
