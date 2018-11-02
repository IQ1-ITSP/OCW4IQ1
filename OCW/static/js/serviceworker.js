var staticCacheName = 'iq1-ocw-cache-v1';

self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(staticCacheName).then(function (cache) {
            console.log("FINDING1");
            return cache.addAll([
                //'/base_layout'
                '/'
            ]);
        })
    );
});

self.addEventListener('fetch', function (event) {
    var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
        if ((requestUrl.pathname === '/')) {
            console.log("Pass1");
            console.log("FINDING2");
            //event.respondWith(caches.match('/base_layout'));
            event.respondWith(caches.match('/'));
            return;
        }
    }
    console.log("Pass2");
    event.respondWith(
        caches.match(event.request).then(function (response) {
            return response || fetch(event.request);
        })
    );
});
