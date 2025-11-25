console.log("SW: Instalando…");

const CACHE = "v1";
const FILES_TO_CACHE = [
    "/", 
    "/static/manifest.json",
    "/static/icons/icon-192.png",
    "/static/icons/icon-512.png"
];

self.addEventListener("install", (event) => {
    console.log("SW: Cacheando archivos…");
    event.waitUntil(
        caches.open(CACHE)
            .then((cache) => cache.addAll(FILES_TO_CACHE))
            .catch((err) => console.error("SW cache error:", err))
    );
    self.skipWaiting();
});

// Activación (limpia versiones viejas)
self.addEventListener("activate", (event) => {
    console.log("SW: Activado");
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key => {
                    if (key !== CACHE) {
                        console.log("SW: Borrando cache viejo:", key);
                        return caches.delete(key);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// Fetch para funcionar offline
self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
