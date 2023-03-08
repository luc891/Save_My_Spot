/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

window.addEventListener('DOMContentLoaded', () => {
    const choice = document.getElementById('account_type')
    choice.addEventListener('change', change_fields);
})

function change_fields() {
    choice = document.getElementById('account_type').value;
    liste = document.querySelectorAll('.field');
    liste.forEach(element => element.style.display = 'none');

    if (choice == 'club')  {
        liste = document.querySelectorAll('.club');
        liste.forEach(element => element.style.display = 'block');
        }
    else
        if (choice == 'approach')   {
        liste = document.querySelectorAll('.approach');
        liste.forEach(element => element.style.display = 'block');
        }
    else
        if (choice == 'airport_manager')    {
        liste = document.querySelectorAll('.airport_man');
        liste.forEach(element => element.style.display = 'block');
        }
    
    document.querySelector('#register_form').style.display = 'block';
}