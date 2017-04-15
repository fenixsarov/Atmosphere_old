$(function () {
    $('.navbar-at').css({
        top: -$('.navbar-at').height(),
        opacity: 0
    }).animate({
        opacity: 1,
        top: 0
    }, 600);

    $(window).scroll(function () {
        if ($(window).scrollTop() > 150) {
            $('nav.navbar.navbar-at')
                .addClass('navbar-at-scroll');
        } else {
            $('nav.navbar.navbar-at')
                .removeClass('navbar-at-scroll');
        }
    });

    $('.portfolio').height($(window).height() - 100);

    $('#portfolio-carousel')
        .find('.caption')
        .animate({
            'left': '4em',
            'opacity': 1
        }, 500, function () {
            $(this).find('.description')
                .animate({
                    'opacity': 1
                }, 500)
        });
    // Carousel
    $('#portfolio-carousel').on('slide.bs.carousel', function () {
        $(this).find('.caption')
            .animate({
                'opacity': 0,
                'left': '50%'
            }, 200, function () {
                $(this).find('.description')
                    .css('opacity', '0');
            });
    });
    $('#portfolio-carousel').on('slid.bs.carousel', function () {
        $(this).find('.caption')
            .animate({
                'left': '4em',
                'opacity': 1
            }, 500, function () {
                $(this).find('.description')
                    .animate({
                        'opacity': 1
                    }, 500)
            });
    });
});