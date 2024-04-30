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

// Скролл вверх страницы
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

// Открытие и закрытие выпадающего меню с книгами на планшетах
function isTouchDevice() {
  return 'ontouchstart' in window || navigator.maxTouchPoints;
}
const headerDrop = document.querySelector('.header__drop');
const headerDropVisibleBox = document.querySelector('.header__drop-links');
if (isTouchDevice() && headerDrop && headerDropVisibleBox) {
  headerDrop.addEventListener('touchstart', () => {
    headerDropVisibleBox.style.display = 'flex';
  });
  document.addEventListener('touchstart', (e) => {
    const isClickInsideDrop = headerDrop.contains(e.target);
    const isDropVisible = headerDropVisibleBox.style.display === 'flex';
    if (!isClickInsideDrop && isDropVisible) {
      headerDropVisibleBox.style.display = 'none';
    }
  });
}

// Прокрутка квадратиков меню разделов до активного
document.addEventListener('DOMContentLoaded', () => {
  const $navItems = document.querySelector('.chapters-nav__list');
  const $navItemActive = document.querySelector('.chapters-nav__item_active');
  if (!$navItems || !$navItemActive) return;
  const navItemsRect = $navItems.getBoundingClientRect();
  const navItemActiveRect = $navItemActive.getBoundingClientRect();
  const navItemsLeft = navItemActiveRect.left - navItemsRect.left + (navItemActiveRect.width - navItemsRect.width) / 2;
  $navItems.scrollLeft = navItemsLeft;
});