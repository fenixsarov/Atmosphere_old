$(function () {
    let $info = $('.photograph-information .desc');
    let $photo = $('div.photo');

    $info.animate({
        'paddingTop': $('.photograph-information').height() / 2 - $info.height() / 2,
        'opacity': 1
    }, 800, function () {
        $(this).find('.photograph-name').animate({
            'opacity': 1
        }, 300);
        $(this).find('.description').animate({
            'opacity': 1
        }, 500);
    });

    $(document).on('mouseenter', 'div.photo',
        function () {
            removePhotoBacking(this);
            let name = $(this).attr('rel');
            $('<h2 class="photo-desc">' + name + '</h2>')
                .appendTo(this)
                .stop()
                .animate({
                    'opacity': 1,
                    'padding-bottom': 0
                }, 500);
            $('<div class="at-backing"></div>')
                .appendTo(this)
                .stop()
                .animate({
                    'opacity': 0.6
                }, 300);
        });
    $(document).on('mouseleave', 'div.photo',
        function () {
            removePhotoBacking(this);
        }
    );

    let photo_path = [
        {"name": 'portrait', "path": '/static/images/photograph/1/galery/portrait/vtmAu3U__w8.jpg'},
        {"name": 'child', "path": '/static/images/photograph/1/galery/child/wQolGrhjWFs.jpg'},
        {"name": 'surprise', "path": '/static/images/photograph/1/galery/surprise/vKsQzRE6HLc.jpg'},
        {"name": 'wedding', "path": '/static/images/photograph/1/galery/wedding/Ijdyz534zu0.jpg'},
        {"name": 'avatars', "path": '/static/images/photograph/1/galery/avatars/9qRsLKDaDo0.jpg'},
        {"name": 'nature', "path": '/static/images/photograph/1/galery/nature/f2am_XG_7PI.jpg'}
    ];

    let $photo_album = $('div.galery');
    
    for (let i = 0; i < photo_path.length - 1 / 2; i+=3) {
        let first_col = Math.floor(Math.random() * (7 - 4)) + 4;
        let second_col = Math.floor(Math.random() * ((10-first_col) - 2)) + 2;
        let third_col = 12 - first_col - second_col;

        $("<a></a>")
            .css({
                'background-image': "url('" + photo_path[i].path + "')"
            })
            .appendTo($photo_album)
            .wrap('<div class="photo col-xs-6 col-sm-' + first_col + '" rel="' + photo_path[i].name + '">');
        $("<a></a>")
            .attr('rel', '')
            .appendTo($photo_album)
            .css({
                'background-image': "url('" + photo_path[i+1].path + "')"
            })
            .wrap('<div class="photo col-xs-6 col-sm-' + second_col + '" rel="' + photo_path[i+1].name + '">');
        $("<a></a>")
            .attr('rel', '')
            .appendTo($photo_album)
            .css({
                'background-image': "url('" + photo_path[i+2].path + "')"
            })
            .wrap('<div class="photo col-xs-6 col-sm-' + third_col + '" rel="' + photo_path[i+2].name + '">');
    }
});

function removePhotoBacking(element) {
    $(element)
        .find('h2.photo-desc')
        .animate({
            'opacity': 0
        }, 300, function () {
            $(this).remove();
        })
        .end()
        .find('div.at-backing')
        .animate({
            'opacity': 0
        }, 300, function () {
            $(this).remove();
        });
}