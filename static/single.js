/* Decodes Base64 encoded URLs on single pages */

(() => {
    mirrors = document.getElementById('mirrors').children
    for(mirror of mirrors){
        link = mirror.firstChild
        url = toURL(decode(link.innerHTML))

        /* Only valid inputs will display */
        if(url){
            link.href = url
            link.innerHTML = url.hostname
        }else{
            mirror.remove();
        }
    }
})();

function decode(encoded){
    try {
        return atob(encoded);
    } catch(e) {
        return false;
    }
}

function toURL(string){
    try {
        return new URL(string)
    } catch(e) {
        return false;
    }
}
