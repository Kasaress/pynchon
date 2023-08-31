// Настройки слайдера с обложками
const swiper = new Swiper('.swiper', {
  effect: 'coverflow',
  grabCursor: true,
  slidesPerView: 3,
  spaceBetween: 0,
  centeredSlides: true,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  coverflowEffect: {
    rotate: 0,
    scale: 0.7,
  }
})

// Открытие и закрытие попапа с обложками
const showBtn = document.querySelector('.other-books__btn');
const coversPopup = document.querySelector('.covers-popup');

showBtn.addEventListener('click', function() {
  coversPopup.classList.add('covers-popup_opened');
  document.addEventListener('keydown', closeCoversPopupEsc)
})

function closeCoversPopup() {
  coversPopup.classList.remove('covers-popup_opened');
  document.removeEventListener('keydown', closeCoversPopupEsc)
}

function closeCoversPopupEsc(evt) {
  if (evt.key === 'Escape') {
    const openedPopup = document.querySelector('.covers-popup_opened');
    closeCoversPopup(openedPopup);
  }
}

coversPopup.addEventListener('mousedown', function(evt) {
  if (evt.target.classList.contains('covers-popup_opened')) {
    closeCoversPopup();
  }
})