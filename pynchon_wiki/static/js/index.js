// Скролл вверх
document.getElementById('scrollToTopLink').addEventListener('click', function(event) {
  event.preventDefault();
  scrollToTop();
});
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

// Выделение активных ссылок в слайдере
function setActiveLink(links, activeClass) {
  links.forEach(link => {
    link.addEventListener('click', event => {
      links.forEach(link => {
        link.classList.remove(activeClass); 
      });
      event.target.classList.add(activeClass); 
    });
  });
}
const commentLinks = document.querySelectorAll('.comment-link');
setActiveLink(commentLinks, 'sidebar__link_active');
const bookLinks = document.querySelectorAll('.book-link');
setActiveLink(bookLinks, 'other-books__book-link_active');