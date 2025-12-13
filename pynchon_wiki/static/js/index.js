// Работа с попапом подтверждения возраста
document.addEventListener('DOMContentLoaded', () => {
  const agePopup = document.getElementById('age-popup');
  const disclaimerPopup = document.getElementById('disclaimer-popup');

  const ageBtn = document.getElementById('age-popup-confirm');
  const disclaimerBtn = document.getElementById('disclaimer-popup-confirm');

  if (!agePopup || !disclaimerPopup || !ageBtn || !disclaimerBtn) return;

  const ageConfirmed = sessionStorage.getItem('ageConfirmed');
  const disclaimerConfirmed = sessionStorage.getItem('disclaimerConfirmed');

  if (!ageConfirmed) {
    agePopup.style.display = 'flex';
  } else if (!disclaimerConfirmed) {
    disclaimerPopup.style.display = 'flex';
  }

  ageBtn.addEventListener('click', () => {
    sessionStorage.setItem('ageConfirmed', 'true');
    agePopup.style.display = 'none';
    disclaimerPopup.style.display = 'flex';
  });

  disclaimerBtn.addEventListener('click', () => {
    sessionStorage.setItem('disclaimerConfirmed', 'true');
    disclaimerPopup.style.display = 'none';
  });
});

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

// Прокрутка пагинатора до активной страницы
document.addEventListener('DOMContentLoaded', () => {
  const $pagItems = document.querySelector('.pagination__block_pages');
  const $pagItemActive = document.querySelector('.pagination__item_active');
  if (!$pagItems || !$pagItemActive) return;
  const pagItemsRect = $pagItems.getBoundingClientRect();
  const pagItemActiveRect = $pagItemActive.getBoundingClientRect();
  const pagItemsLeft = pagItemActiveRect.left - pagItemsRect.left + (pagItemActiveRect.width - pagItemsRect.width) / 2;
  $pagItems.scrollLeft = pagItemsLeft;
});