// Анимация ракеты
// let circle = document.querySelector('.promo__circle');
// let rocket = document.querySelector('.promo__rocket');
// window.onscroll = magic;
// function magic() {
//   if (window.innerWidth >= 768) {
//     circle.style.width = `${23.75 + window.pageYOffset * 0.7}vw`;
  
//     circle.style.bottom = `${6.39 - window.pageYOffset * 0.1}vw`;
//     circle.style.right = `${10.56 - window.pageYOffset * 0.2}vw`;
  
//     rocket.style.bottom = `${0.49 + window.pageYOffset * 0.1}vw`;
//     rocket.style.right = `${9.17 - window.pageYOffset * 0.1}vw`;
//   }
// }

// Счётчик
function animateValue(obj, start, end, duration) {
let startTimestamp = null;
const step = (timestamp) => {
  if (!startTimestamp) startTimestamp = timestamp;
  const progress = Math.min((timestamp - startTimestamp) / duration, 1);
  obj.innerHTML = Math.floor(progress * (end - start) + start);
  if (progress < 1) {
    window.requestAnimationFrame(step);
  }
};
window.requestAnimationFrame(step);
}
const obj = document.getElementById('value');
animateValue(obj, 99999, 00000, 50000000);



//Появление текста из-под оверлея
// const overlays = document.querySelectorAll('.chapter__overlay');
// function onEntry(entry) {
//   entry.forEach(change => {
//     if(change.isIntersecting) {
//       let rect = change.getBoundingClientRect(),
//       scrollTop = window.pageYOffset || document.documentElement.scrollTop;
//       let distanceTop = rect.top + scrollTop;
//       let elHeight = change.target.style.height
//       change.target.style.height = `${elHeight + distanceTop - window.pageYOffset}px`;
//     }
//   })
// }
// let options = { threshold: [0.5]};
// let observer = new IntersectionObserver(onEntry, options);
// for (let item of overlays) {
//   observer.observe(item);
// }