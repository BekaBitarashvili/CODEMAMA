document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const authIcons = document.querySelector('.auth-icons');
    const searchBar = document.querySelector('.search-bar');

    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        authIcons.classList.toggle('active');
        searchBar.classList.toggle('active');
    });
});
