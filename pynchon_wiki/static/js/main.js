// Анимация ракеты
let circle = document.querySelector('.promo__circle');
let rocket = document.querySelector('.promo__rocket');
window.onscroll = magic;
function magic() {
  if (window.innerWidth >= 768) {
    circle.style.width = `${23.75 + window.pageYOffset * 0.7}vw`;
  
    circle.style.bottom = `${6.39 - window.pageYOffset * 0.1}vw`;
    circle.style.right = `${10.56 - window.pageYOffset * 0.2}vw`;
  
    rocket.style.bottom = `${0.49 + window.pageYOffset * 0.1}vw`;
    rocket.style.right = `${9.17 - window.pageYOffset * 0.1}vw`;
  } else {
    circle.style.width = `${252 + window.pageYOffset * 3}px`;
  
    circle.style.bottom = `${100.8 - window.pageYOffset}px`;
    circle.style.right = `${30.74 - window.pageYOffset}px`;
  
    rocket.style.bottom = `${38 + window.pageYOffset}px`;
    rocket.style.right = `${16 - window.pageYOffset}px`;
  }
}

// Счётчик

// function animateValue(obj, start, end, duration) {
// let startTimestamp = null;
// const step = (timestamp) => {
//   if (!startTimestamp) startTimestamp = timestamp;
//   const progress = Math.min((timestamp - startTimestamp) / duration, 1);
//   obj.innerHTML = Math.floor(progress * (end - start) + start);
//   if (progress < 1) {
//     window.requestAnimationFrame(step);
//   }
// };
// window.requestAnimationFrame(step);
// }
// const obj = document.getElementById('value');
// animateValue(obj, 99999, 00000, 50000000);


function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    const value = Math.floor(progress * (end - start) + start);

    const formattedValue = String(value).padStart(5, '0');
    
    obj.innerHTML = formattedValue;
    
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

// Функция, которая будет запускать анимацию при достижении блока
function startCounterAnimation() {
  const obj = document.getElementById('value');
  animateValue(obj, 99999, 0, 3000);
}

// Функция для проверки, виден ли блок на экране
function isElementInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Обработчик события прокрутки страницы
function onScroll() {
  const counterBlock = document.querySelector('.chapter-preview__counter');
  
  if (isElementInViewport(counterBlock)) {
    startCounterAnimation();
    // Удаляем обработчик события после запуска анимации, если это нужно
    window.removeEventListener('scroll', onScroll);
  }
}

// Добавляем обработчик события прокрутки
window.addEventListener('scroll', onScroll);