// Работа с попапом подтверждения возраста
const agePopup = document.querySelector('.age-popup');
const ageBtn = agePopup.querySelector('.age-popup__button');

if (!localStorage.getItem('visited') || !localStorage.getItem('age-confirm')) {
  if (agePopup) agePopup.style.display = 'flex';
  localStorage.setItem('visited', 'true');
  setTimeout(function () {
    localStorage.removeItem('visited');
  }, 24 * 60 * 60 * 1000);
}

if (ageBtn) ageBtn.addEventListener('click', () => {
  agePopup.style.display = 'none';
  localStorage.setItem('age-confirm', 'true');
  setTimeout(function () {
    localStorage.removeItem('age-confirm');
  }, 24 * 60 * 60 * 1000);
})

// Скролл вверх
document.getElementById('scrollToTopLink').addEventListener('click', function (event) {
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