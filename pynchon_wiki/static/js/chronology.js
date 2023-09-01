// Настройка слайдера дат

const slider = new Swiper('.swiper1', {
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
  breakpoints: {
    1024: {
      spaceBetween: 14,
      // direction: 'horizontal',
    }
  }
})

const slides = document.querySelectorAll('.chronology__slide-text');

slider.on('slideChange', () => {
  for (const slide of slides) {
    if (slide.textContent.length > 10) {
      slide.classList.add('chronology__slide_s')
    }
  }
})

const factContainers = document.querySelectorAll('.chronology__fact');
slider.on('slideChange', () => {
    const activeSlideId = slider.slides[slider.activeIndex].dataset.id;
    
    factContainers.forEach(container => {
        if (container.dataset.id === activeSlideId) {
            container.style.display = 'block';
        } else {
            container.style.display = 'none';
        }
    });
});

function setDefaultFact() {
  factContainers.forEach(container => {
    container.style.display = 'none';
  });

  factContainers[0].style.display = 'block';
}
setDefaultFact();

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