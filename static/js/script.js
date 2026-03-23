(function(){

  // ── Manifest ─────────────────────────
  const manifest = {
    name: "Uncle Moro Varadero Food Truck",
    short_name: "Uncle Moro",
    description: "Authentic Cuban & Street Food",
    start_url: "/",
    display: "standalone",
    background_color: "#003d6b",
    theme_color: "#0096c7",
    orientation: "portrait-primary",
    icons: [
      {
        src: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 192 192'><rect width='192' height='192' rx='32' fill='%230096c7'/><text y='.85em' font-size='140' x='20'>🌮</text></svg>",
        sizes: "192x192",
        type: "image/svg+xml"
      }
    ]
  };

  const blob = new Blob([JSON.stringify(manifest)], {type:'application/manifest+json'});
  const url = URL.createObjectURL(blob);

  const link = document.createElement('link');
  link.rel = 'manifest';
  link.href = url;

  document.head.appendChild(link);


  // ── Service Worker ─────────────────────────

  const swCode = `
    const CACHE = 'uncle-moro-v1';

    self.addEventListener('install', event => {
      self.skipWaiting();
    });

    self.addEventListener('activate', event => {
      self.clients.claim();
    });

    self.addEventListener('fetch', event => {
      event.respondWith(fetch(event.request).catch(() => caches.match(event.request)));
    });
  `;

  if ('serviceWorker' in navigator) {

    const swBlob = new Blob([swCode], {type:'text/javascript'});
    const swUrl = URL.createObjectURL(swBlob);

    navigator.serviceWorker.register(swUrl).catch(()=>{});
  }


  // ── PWA Banner ─────────────────────────

  let deferredPrompt = null;

  window.addEventListener('beforeinstallprompt', e => {
    e.preventDefault();
    deferredPrompt = e;

    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'flex';
  });

  window._installPWA = function(){

    if (deferredPrompt){
      deferredPrompt.prompt();
      deferredPrompt = null;
    }

    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'none';
  }

  window._dismissBanner = function(){

    const banner = document.getElementById('pwa-banner');
    if (banner) banner.style.display = 'none';
  }

})();


// ── CREAR TARJETAS DE PLATOS ─────────────────

const grid = document.querySelector('.grid');

if(grid){

  Object.keys(DISHES).forEach(id => {

    const d = DISHES[id];

    const card = document.createElement('a');

    // ⭐ AQUÍ ESTÁ LA PARTE IMPORTANTE
    card.href = `/plates?plate=${id}`;

    card.className = 'card';

    card.innerHTML = `
      <div class="card-name">${d.name}</div>
      <div class="card-desc">${d.desc}</div>
      <div class="card-btm">
        <span class="price">${d.price}</span>
      </div>
    `;

    grid.appendChild(card);

  });

}