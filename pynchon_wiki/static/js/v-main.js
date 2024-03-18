// Анимация створок Венеры
let leftPart = document.getElementById('silhouette-left');
let rightPart = document.getElementById('silhouette-right');
let promoText = document.getElementById('v-promo-text');
let dot = document.querySelector('.promo__v-dot');

window.onScroll = magicV;

function magicV() {
  const scrollTop = window.pageYOffset;

  leftPart.style.transform = `rotate(${- 170 + 170 / (scrollTop/200 + 1)}deg)`;
  rightPart.style.transform = `rotate(${170 - 170 / (scrollTop/200 + 1)}deg)`;
  promoText.style.opacity = `${1/(scrollTop + 1)}`;

  const startOffset = 0;
  const endOffset = 800;

  const progress = (scrollTop - startOffset) / (endOffset - startOffset);

  if (progress <= 0.1) {
    dot.style.transform = `translateY(${- 70 * 10 * progress}px)`;
  } else if (progress <= 0.2) {
    dot.style.transform = `translateY(${-70 + (70 * 10 * (progress - 0.1))}px)`;
  } else if (progress <= 0.3) {
    dot.style.transform = `translateY(${- 20 * 10 * (progress - 0.2)}px)`;
  } else if (progress <= 0.4) {
    dot.style.transform = `translateY(${-20 + (20 * 10 * (progress - 0.3))}px)`;
  } else {
    dot.style.transform = `translateX(${50 * 10 * (progress - 0.4)}vw)`;
  }
}

// Добавляем обработчик события прокрутки
window.addEventListener('scroll', onScroll);