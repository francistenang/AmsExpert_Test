/*const toggleBtn = document.getElementById('toggleBtn')

toggleBtn.addEventListener('click', function (e) {
    const sideMenu = document.getElementById('sideMenu')
    const main = document.getElementById('main')
    if (!sideMenu.classList.contains('close')) {
        toggleBtn.classList.toggle('rotate')
        sideMenu.classList.toggle('close')
        main.classList.toggle('increase_size')
    } else {
        toggleBtn.classList.toggle('rotate')
        sideMenu.classList.toggle('close')
        main.classList.toggle('increase_size')
    }
    if menu is open then close it
    console.log(e)
    else open it
})*/

const toggleSmallMenu = document.getElementById('toggleSmallMenu')

toggleSmallMenu.addEventListener('click', function (e) {
    const sideMenus = document.getElementById('sideMenu')
    if(!sideMenus.classList.contains('tablet-side-bar-open')) {
        sideMenus.classList.toggle('tablet-side-bar-open')
    } else {
        sideMenus.classList.toggle('tablet-side-bar-open')
    }
})

document.addEventListener('click', function (e) {
    if (e.target.classList.contains('image-profile')) {
        let dropdownMenu = document.getElementById('dropdown')
        dropdownMenu.classList.toggle('is-active')
        console.log(e.target)
    } else {
        let dropdownMenu = document.getElementById('dropdown')
        if (dropdownMenu.classList.contains('is-active')) {
            dropdownMenu.classList.toggle('is-active')
        }
    }
})

let dropdown = document.querySelector('.dropdown');
dropdown.addEventListener('click', function(event) {
    event.stopPropagation();
    dropdown.classList.toggle('is-active');
});