$(document).ready(function() {
    // при скролле показываем или скрываем кнопку наверх
    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    });

    // при клике на кнопку наверх плавно прокручиваем страницу вверх
    $('.back-to-top').click(function() {
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
});