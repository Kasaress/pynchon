// Работа с попапом подтверждения возраста
const agePopup = document.querySelector('.age-popup');
const ageBtn = agePopup.querySelector('.age-popup__button');

if (!localStorage.getItem('visited') || !localStorage.getItem('age-confirm')) {
  if (agePopup) agePopup.style.display = 'flex';
  localStorage.setItem('visited', 'true');
  setTimeout(function() {
    localStorage.removeItem('visited');
  }, 24 * 60 * 60 * 1000);
}

if (ageBtn) ageBtn.addEventListener('click', () => {
  agePopup.style.display = 'none';
  localStorage.setItem('age-confirm', 'true');
  setTimeout(function() {
    localStorage.removeItem('age-confirm');
  }, 24 * 60 * 60 * 1000);
})

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

// Открытие и закрытие меню
const menu = document.querySelector('.menu');
const menus = document.querySelectorAll('.menu');
const burger = document.querySelector('.header__button');

function openMenu(menu) {
  menu.classList.add('menu_opened');
}

function closeMenu(menu) {
  menu.classList.remove('menu_opened');
}

menus.forEach(function (menu) {
  menu.addEventListener('mousedown', function (evt) {
    if (evt.target.classList.contains('menu_opened') || evt.target.classList.contains('menu__close')) {
      closeMenu(menu);
    }
  })
})

burger.addEventListener('click', function () { openMenu(menu) });

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

document.addEventListener("DOMContentLoaded", function () {
  var buttons = document.querySelectorAll('.chapter-button');
  var contentContainer = document.getElementById('comments-content');
  var prevButton = document.getElementById('prev-chapter');
  var nextButton = document.getElementById('next-chapter');

  var currentChapterIndex = 0;
  var chapters = Array.from(buttons).map(button => button.dataset.chapterId);

  var pageKey = window.location.pathname;
  var savedChapterId = localStorage.getItem('selectedChapterId_' + pageKey);
  if (savedChapterId && chapters.indexOf(savedChapterId) !== -1) {
    loadChapter(savedChapterId, buttons[chapters.indexOf(savedChapterId)].getAttribute('data-view-page'))
      .then(() => scrollToChapter(savedChapterId));
  } else {
    loadChapter(chapters[0], buttons[0].getAttribute('data-view-page'));
  }

  function loadChapter(chapterId, viewPage) {
    return new Promise(function (resolve, reject) {
      if (currentChapterIndex !== chapters.indexOf(chapterId)) {
        fetch(`/${viewPage}?chapter_id=${chapterId}`)
          .then(response => response.text())
          .then(content => {
            localStorage.setItem('selectedChapterId_' + pageKey, chapterId);
            contentContainer.innerHTML = content;
            buttons[currentChapterIndex].classList.remove('active');
            buttons[chapters.indexOf(chapterId)].classList.add('active');
            currentChapterIndex = chapters.indexOf(chapterId);
            updateNavigationButtons();
            var chapterButton = document.querySelector(`.chapter-button[data-chapter-id="${chapterId}"]`);
            chapterButton.scrollIntoView({ behavior: "smooth", block: "start" });           
            resolve();
          })
          .catch(error => {
            console.error("Ошибка при загрузке контента:", error);
            reject(error);
          });
      } else {
        updateNavigationButtons();
        resolve();
      }
    });
  }

  function updateNavigationButtons() {
    prevButton.disabled = currentChapterIndex === 0;
    nextButton.disabled = currentChapterIndex === chapters.length - 1;
  }

  function scrollToChapter(chapterId) {
    return new Promise(function (resolve) {
      var notesContent = document.querySelector('.chapter-2-3-notes__content');
      var chapterButton = document.querySelector(`.chapter-button[data-chapter-id="${chapterId}"]`);

      var buttonOffsetTop = chapterButton.offsetTop;
      var containerScrollTop = notesContent.scrollTop;
      var targetScrollTop = buttonOffsetTop - containerScrollTop;

      requestAnimationFrame(function () {
        notesContent.scrollTo({
          top: targetScrollTop,
          behavior: 'smooth'
        });
        resolve();
      });
    });
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      var selectedChapterId = button.dataset.chapterId;
      var selectedViewPage = button.getAttribute('data-view-page');

      loadChapter(selectedChapterId, selectedViewPage)
        .then(() => scrollToChapter(selectedChapterId));
    });
  });

  prevButton.addEventListener('click', function () {
    if (currentChapterIndex > 0) {
      var prevChapterId = chapters[currentChapterIndex - 1];
      var prevViewPage = buttons[currentChapterIndex - 1].getAttribute('data-view-page');

      loadChapter(prevChapterId, prevViewPage)
        .then(() => scrollToChapter(prevChapterId));
    }
  });

  nextButton.addEventListener('click', function () {
    if (currentChapterIndex < chapters.length - 1) {
      var nextChapterId = chapters[currentChapterIndex + 1];
      var nextViewPage = buttons[currentChapterIndex + 1].getAttribute('data-view-page');

      loadChapter(nextChapterId, nextViewPage)
        .then(() => scrollToChapter(nextChapterId));
    }
  });
});

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

document.getElementById('scrollToTopLink').addEventListener('click', function(event) {
  event.preventDefault();
  scrollToTop();
});