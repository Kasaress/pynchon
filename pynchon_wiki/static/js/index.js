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
  var prevButton = document.getElementById('prev-chapter');
  var nextButton = document.getElementById('next-chapter');

  var currentChapterIndex = 0;
  var chapters = Array.from(buttons).map(button => button.dataset.chapterId);

  function loadChapter(chapterId, viewPage) {
    fetch(`/${viewPage}?chapter_id=${chapterId}`)
      .then(response => response.text())
      .then(content => {
        contentContainer.innerHTML = content;
        currentChapterIndex = chapters.indexOf(chapterId);
        updateNavigationButtons();
      })
      .catch(error => console.error("Ошибка при загрузке контента:", error));
  }

  function updateNavigationButtons() {
    prevButton.disabled = currentChapterIndex === 0;
    nextButton.disabled = currentChapterIndex === chapters.length - 1;
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      var selectedChapterId = button.dataset.chapterId;
      var selectedViewPage = button.getAttribute('data-view-page');
      loadChapter(selectedChapterId, selectedViewPage);
    });
  });

  prevButton.addEventListener('click', function () {
    if (currentChapterIndex > 0) {
      var prevChapterId = chapters[currentChapterIndex - 1];
      var prevViewPage = buttons[currentChapterIndex - 1].getAttribute('data-view-page');
      loadChapter(prevChapterId, prevViewPage);
    }
  });

  nextButton.addEventListener('click', function () {
    if (currentChapterIndex < chapters.length - 1) {
      var nextChapterId = chapters[currentChapterIndex + 1];
      var nextViewPage = buttons[currentChapterIndex + 1].getAttribute('data-view-page');
      loadChapter(nextChapterId, nextViewPage);
    }
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

// Обработчики клика по кнопкам "Мероприятий"
const plannedMeetingsButton = document.getElementById('plannedMeetingsButton');
const pastMeetingsButton = document.getElementById('pastMeetingsButton');
const plannedMeetingsContainer = document.getElementById('plannedMeetingsContainer');
const pastMeetingsContainer = document.getElementById('pastMeetingsContainer');

plannedMeetingsButton.addEventListener('click', function () {
  plannedMeetingsContainer.style.display = 'block';
  pastMeetingsContainer.style.display = 'none';
});
pastMeetingsButton.addEventListener('click', function () {
  plannedMeetingsContainer.style.display = 'none';
  pastMeetingsContainer.style.display = 'block';
});