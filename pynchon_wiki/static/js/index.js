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

// Получение динамического контента для вывода комментариев и описания глав
document.addEventListener("DOMContentLoaded", function () {
  var buttons = document.querySelectorAll('.chapter-button');
  var contentContainer = document.getElementById('comments-content');

  buttons.forEach(function (button) {
    button.addEventListener('click', async function () {
      var selectedChapterId = button.dataset.chapterId;
      var viewPage = button.dataset.viewPage;

      try {
        var response = await fetch(`/${viewPage}?chapter_id=${selectedChapterId}`);
        contentContainer.innerHTML = await response.text();
      } catch (error) {
        console.error("Ошибка при загрузке контента:", error);
      }
    });
  });
});

// Автоматическое закрытие вкладок с названием глав в аккордеоне, при нажатии на новую
document.addEventListener('DOMContentLoaded', function() {
  const accordionButtons = document.querySelectorAll('.accordion-button');
  accordionButtons.forEach(button => {
    button.addEventListener('click', () => {
      accordionButtons.forEach(otherButton => {
        if (otherButton !== button && otherButton.getAttribute('aria-expanded') === 'true') {
          otherButton.click();
        }
      });
    });
  });
});