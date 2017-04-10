$(function () {
    $('#portfolio-carousel .carousel-inner').height($(window).height());

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