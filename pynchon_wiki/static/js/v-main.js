// Анимация створок Венеры
let leftPart = document.getElementById('silhouette-left');
let rightPart = document.getElementById('silhouette-right');
let promoText = document.getElementById('v-promo-text');
let dot = document.querySelector('.promo__v-dot');

window.onScroll = magicV;

function magicV() {
  leftPart.style.transform = `rotate(${- 170 + 170 / (window.pageYOffset/200 + 1)}deg)`;
  rightPart.style.transform = `rotate(${170 - 170 / (window.pageYOffset/200 + 1)}deg)`;
  promoText.style.opacity = `${1/(window.pageYOffset + 1)}`;
  if (window.pageYOffset > 2) {
    dot.style.animation = 'pointBounce 2s ease-out forwards';
  }
}

// Добавляем обработчик события прокрутки
window.addEventListener('scroll', onScroll);