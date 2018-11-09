var staticCacheName = 'iq1-ocw-cache-v1';

self.addEventListener('install', function (event) {
    console.log("INSTALL EVENT", event);  // event.currentTarget.registration.scope
    event.waitUntil(
        caches.open(staticCacheName).then(function (cache) {
            return cache.addAll([
                //'/base_layout'
                '/',
                '/lecture/?code=PHY.Q206'
            ]);
        })
    );
});

self.addEventListener('fetch', function (event) {
    //console.log("FETCH EVENT", event);
    var requestUrl = new URL(event.request.url);
    //console.log("REQUESTURL.ORIGIN", requestUrl.origin);

    var referrer = event.request.referrer
    console.log("EVENT.REQUEST", referrer);
    var reff_start = referrer.indexOf('/lecture');
    if (reff_start === -1) {
        reff_start = referrer.indexOf('/result');
    }
    if (reff_start === -1) {
        reff_start = referrer.indexOf('/department');
    }
    if (reff_start > -1) {
        var req_path = referrer.slice(reff_start);
        console.log("REQ_PATH", req_path);
        caches.open(staticCacheName).then(function (cache) {
            return cache.addAll([
                req_path
            ]);
        })
    }
    //console.log("REQUESTURL.PATHNAME", requestUrl.pathname);
    if (requestUrl.origin === location.origin) {
        if ((requestUrl.pathname === '/')) {
            //event.respondWith(caches.match('/base_layout'));
            event.respondWith(caches.match('/'));
            return;
        }/*
        else if (requestUrl.pathname.indexOf('/lecture') === 0) {
            console.log("LECTURE", requestUrl.pathname);
            caches.open(staticCacheName).then(function (cache) {
                return cache.addAll([
                    requestUrl.pathname
                ]);
            })
        }*/
    }
    event.respondWith(
        caches.match(event.request).then(function (response) {
            return response || fetch(event.request);
        })
    );
});
