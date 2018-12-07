var staticCacheName = 'iq1-ocw-cache-v1';

self.addEventListener('install', function (event) {
    // console.log("INSTALL EVENT", event);  // event.currentTarget.registration.scope
    event.waitUntil(
        caches.open(staticCacheName).then(function (cache) {
            return cache.addAll([
                //'/base_layout'
                '/',
            ]);
        })
    );
});

self.addEventListener('fetch', function (event) {
    // GETメソッド以外は無視
    if (event.request.method !== 'GET') return;

    var requestUrl = new URL(event.request.url);
    // console.log("requestUrl", requestUrl);

    let url = event.request.url;
    // console.log("EVENT.REQUEST.URL", event.request.url);

    var referrer = event.request.referrer
    // console.log("EVENT.REQUEST.REFERRER", referrer);

    if (requestUrl.origin === location.origin) {
        if ((requestUrl.pathname === '/')) {
            //event.respondWith(caches.match('/base_layout'));
            event.respondWith(caches.match('/'));
            return;
        }
    }

    event.respondWith(

        caches.open(staticCacheName)
          .then(cache =>{

            return cache.match(event.request)
              .then(response => {

                // キャッシュファイルがある
                if (response) {
                  console.log('CACHE FETCH:', url);
                  return response;
                }
                // キャッシュファイルがない
                return fetch(event.request)
                  .then(newreq => {
                    console.log('NETWORK FETCH:', url);
                    if (newreq.ok) cache.put(event.request, newreq.clone());
                    return newreq;
                  });
              });
          })
    );
});
