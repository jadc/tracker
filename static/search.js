document.addEventListener('DOMContentLoaded', () => {
    const pages = document.querySelectorAll('a');
    const search = document.getElementById('search');

    search.addEventListener('input', () => {
        const query = clean(search.value).split(' ');

        pages.forEach(page => {
            const matchable = [
                page.getElementsByTagName('h1')[0].innerHTML,
                page.dataset.tags
            ];
            const toMatch = clean(matchable.join(' '));
            const isMatch = query.every(term => toMatch.includes(term));

            page.style.display = isMatch ? 'flex' : 'none';
        });
    });
    console.log('loaded search bar');
})

function clean(input){
    return input.toLowerCase().trim().normalize('NFD');
}
