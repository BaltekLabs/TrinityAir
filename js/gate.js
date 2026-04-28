(async function () {
    const EXPECTED = 'c7a545be42d4f639fbc2f744406e37a97bc2089f7d3c20ee14aa03096e7c363c';
    const KEY = 'ta_access';

    if (sessionStorage.getItem(KEY) === EXPECTED) return;

    // Build relative path back to root-level access.html based on directory depth
    const parts = window.location.pathname.split('/').filter(p => p.length > 0);
    const depth = parts.length - 1;
    const prefix = depth > 0 ? '../'.repeat(depth) : '';

    window.location.replace(prefix + 'access.html?return=' + encodeURIComponent(window.location.pathname));
})();
