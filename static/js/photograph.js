$(function () {
    var $info = $('.photograph-information .desc');
    var $photo = $('div.photo');

    setPhotographPhoto('1');

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
            var name = $(this).attr('rel');
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

    var photo_path = [
        {"name": 'portrait', "path": '/static/images/photograph/1/galery/portrait/vtmAu3U__w8.jpg'},
        {"name": 'child', "path": '/static/images/photograph/1/galery/child/wQolGrhjWFs.jpg'},
        {"name": 'surprise', "path": '/static/images/photograph/1/galery/surprise/vKsQzRE6HLc.jpg'},
        {"name": 'wedding', "path": '/static/images/photograph/1/galery/wedding/Ijdyz534zu0.jpg'},
        {"name": 'avatars', "path": '/static/images/photograph/1/galery/avatars/9qRsLKDaDo0.jpg'},
        {"name": 'nature', "path": '/static/images/photograph/1/galery/nature/f2am_XG_7PI.jpg'}
    ];

    var $photo_album = $('div.galery');
    
    for (var i = 0; i < photo_path.length - 1 / 2; i+=3) {
        var first_col = Math.floor(Math.random() * (7 - 4)) + 4;
        var second_col = Math.floor(Math.random() * ((10-first_col) - 2)) + 2;
        var third_col = 12 - first_col - second_col;

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

    fillCalendarDays();
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

function setPhotographPhoto(name) {
    $('.photograph-img').find('img')
        .attr('src', '/static/images/photograph/' + name + '/person.png');
}

function fillCalendarDays(chooseMonth) {
    // Месяц текущий, или следующий
    var d = new Date();
    var year = d.getFullYear();
    var month = d.getUTCMonth();
    var today = d.getDate();
    var first_day = new Date(year,month,1);
    var first_wday = first_day.getDay();
    var oneHour = 1000 * 60 * 60; // вычисляем количество миллисекунд в 1 часе
    var oneDay = oneHour * 24; // вычисляем количество миллисекунд в одних сутках
    var nextMonth = new Date(year, month + 1, 1); // устанавливаем дату первого числа следующего месяца 
    var last_date = Math.ceil((nextMonth.getTime() - first_day.getTime() - oneHour)/oneDay);// вычисляем крайний день текущего месяца

    var $calendar = $('.at-calendar-table');

    var $table_row = $('<tr class="at-calendar-week"></tr>');
    var $table_col = $("<td></td>");
    var month_day = 1;

    for(var i = 1;; i++) {
        if(month_day === last_date) {
            $table_col.append('<button class="at-calendar-day-btn">' + month_day + '</button>');
            $table_row.append($table_col.clone());
            $calendar.append($table_row.clone());
            $table_row.empty();
            $table_col.empty();
            break;
        }

        if (i >= first_wday) {
            $table_col.append('<button class="at-calendar-day-btn">' + month_day + '</button>');
            month_day++;
        }
        $table_row.append($table_col.clone());
        $table_col.empty();

        if (i % 7 === 0) {
            $calendar.append($table_row.clone());
            $table_row.empty();
        }
    }

}