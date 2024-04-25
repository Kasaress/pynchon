// Скрипты управления примечаниями и комментариями

document.addEventListener("DOMContentLoaded", function () {
  const pageKey = window.location.pathname;
  const chapterButtons = document.querySelectorAll('.chapter-button');
  const collapses = document.querySelectorAll('.accordion-collapse');
  const commentLinks = document.querySelectorAll('.sidebar__link');
  const contentContainer = document.getElementById('comments-content');
  const prevButton = document.getElementById('prev-chapter');
  const nextButton = document.getElementById('next-chapter');

  const chapters = Array.from(chapterButtons).map(button => button.dataset.chapterId);
  let currentIndex;
  let savedChapterId = localStorage.getItem('selectedChapterId_' + pageKey);

  // Проверка наличия сохраненной главы в localStorage и отрисовка первоначального массива элементов контента

  if (savedChapterId && chapters.indexOf(savedChapterId) !== -1) {
    loadChapter(
      savedChapterId,
      chapterButtons[chapters.indexOf(savedChapterId)].getAttribute('data-view-page')
    )
  } else {
    loadChapter(
      chapters[0],
      chapterButtons[0].getAttribute('data-view-page')
    );
  }

  // Загрузка главы
  function loadChapter(chapterId, viewPage) {
    return new Promise(function (resolve, reject) {
      if (currentIndex !== chapters.indexOf(chapterId)) {
        fetch(`/${viewPage}?chapter_id=${chapterId}`)
          .then(response => response.text())
          .then(content => {
            localStorage.setItem('selectedChapterId_' + pageKey, chapterId); // сохраняем главу в хранилище
            contentContainer.innerHTML = content; // обновляем контент
            contentContainer.scrollTop = 0; // скроллим в начало новой главы
            $(collapses[currentIndex]).collapse('hide'); // скрываем пред. пункт в меню
            currentIndex = chapters.indexOf(chapterId); // перезаписываем текущий индекс главы
            $(collapses[currentIndex]).collapse('show'); // открываем новый пункт в меню
            updateNavigationButtons(); // проверяем состояние кнопок пред. и след. глав
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
    })
  };

  // Блокировка кнопок в начале и конце массива
  function updateNavigationButtons() {
    prevButton.disabled = currentIndex === 0;
    nextButton.disabled = currentIndex === chapters.length - 1;
  };

  // Слушатели 
  chapterButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      const chapterId = button.dataset.chapterId;
      const viewPage = button.getAttribute('data-view-page');
      loadChapter(chapterId, viewPage);
    })
  });

  nextButton.addEventListener('click', function () {
    if (currentIndex < chapters.length - 1) {
      const nextChapterId = chapters[currentIndex + 1];
      const nextViewPage = chapterButtons[currentIndex + 1].getAttribute('data-view-page');
      loadChapter(nextChapterId, nextViewPage);
    }
  });

  prevButton.addEventListener('click', function () {
    if (currentIndex > 0) {
      const prevChapterId = chapters[currentIndex - 1];
      const prevViewPage = chapterButtons[currentIndex - 1].getAttribute('data-view-page');
      loadChapter(prevChapterId, prevViewPage);
    }
  });

  commentLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      const commentId = link.getAttribute('href');
      const comment = document.getElementById(`${commentId.slice(1)}`);
      contentContainer.scrollBy({
        top: $(comment).position().top,
        left: 0,
        behavior: 'smooth'
      })
      console.log($(comment).position().top);
    })
  })
});