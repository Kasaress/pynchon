// Настройки слайдера с обложками
const swiper = new Swiper('.swiper', {
    slidesPerView: 'auto',
    spaceBetween: 16,
    navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev'
    }
})