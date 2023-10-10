// Настройка слайдера дат

const swiper = new Swiper('.swiper', {
  mousewheel: true,
  slidesPerView: 3,
  spaceBetween: 18,
  centeredSlides: true,
  loop: true,
  direction: 'vertical',
  autoHeight: true,
  slideActiveClass: 'chronology__slide_active',
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev'
  },
})


const slides = document.querySelectorAll('.chronology__slide-text');

swiper.on('slideChange', () => {
  for (const slide of slides) {
    if (slide.textContent.length > 10) {
      slide.classList.add('chronology__slide_s')
    }
  }
})

// Управление разворачиванием и сворачиванием текста

const facts = document.querySelectorAll('.chronology-description__fact');

facts.forEach((fact) => {
  const text = fact.querySelector('.chronology-description__fact-text');
  const button = fact.querySelector('.chronology-description__fact-btn');
  const moreText = 'читать дальше';
  const collapseText = 'свернуть';

  if (text.scrollHeight > 130) {
    button.style.display = 'block';
  }

  button.addEventListener('click', () => {
    if (button.textContent !== collapseText) {
      text.style.height = 'auto';
      button.textContent = collapseText;
    } else if (button.textContent === collapseText) {
      text.style.height = '130px';
      button.textContent = moreText;
    }
  })

})
