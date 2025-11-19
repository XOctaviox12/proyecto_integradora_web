console.log("SW: Instalando…");

const CACHE = "v1";
const FILES_TO_CACHE = [
    "/", 
    "/static/manifest.json"
];

self.addEventListener("install", (event) => {
    console.log("SW: Cacheando archivos…");
    event.waitUntil(
        caches.open(CACHE)
            .then((cache) => cache.addAll(FILES_TO_CACHE))
            .catch((err) => console.error("SW cache error:", err))
    );
});
