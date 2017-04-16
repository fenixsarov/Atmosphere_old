$(function () {
    $('.at-navbar').css({
        top: -$('.at-navbar').height(),
        opacity: 0
    }).animate({
        opacity: 1,
        top: 0
    }, 600);
    
    $('.slide-btn')
        .on('click', function () {
            if ($(this).hasClass('at-navbar-show')) {
                $(this)
                    .removeClass('at-navbar-show')
                    .parent()
                    .animate({
                        'left': 0
                    }, 300, function () {
                        $('body').css({
                            'overflow': 'hidden'
                        });
                    });
            } else {
                $(this)
                    .addClass('at-navbar-show')
                    .parent()
                    .animate({
                        'left': '-205px'
                    }, 300, function () {
                        $('body').css({
                            'overflow': 'auto'
                        });
                    });
            }
        });

    $(window).scroll(function () {
        if ($(window).scrollTop() > 150) {
            $('nav.navbar.at-navbar')
                .addClass('at-navbar-scroll');
        } else {
            $('nav.navbar.at-navbar')
                .removeClass('at-navbar-scroll');
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