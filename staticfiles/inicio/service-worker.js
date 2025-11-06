const CACHE_NAME = 'estrella-cache-v1';
const urlsToCache = [
  '/',
  '/static/inicio/css/styles.css',
  '/static/inicio/js/main.js'
  // agrega más recursos si los necesitas
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
