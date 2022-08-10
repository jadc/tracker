/* Decodes Base64 encoded URLs on single pages */

(() => {
    for(mirror of document.getElementsByClassName('mirror')){
        url = toURL(decode(mirror.innerHTML))

        /* Only valid inputs will display */
        if(url){
            mirror.href = url
            mirror.innerHTML = url.hostname
        }else{
            mirror.remove();
            console.error(`Failed to decode mirror with string '${link.innerHTML}'`)
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
