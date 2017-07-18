from django.shortcuts import render

debug_flag = True


def main(request):
    debug = debug_flag
    page = 'index'
    return render(request, 'index.html', locals())


def about(request):
    debug = debug_flag
    page = 'about'
    return render(request, 'about.html', locals())


def photograph(request):
    debug = debug_flag
    page = 'photograph'
    return render(request, 'photograph.html', locals())


def photographs(request):
    debug = debug_flag
    page = 'photographs'
    # Временно отрисовывается персональная страница фотографа
    return render(request, 'photograph.html', locals())


def contacts(request):
    debug = debug_flag
    page = 'contacts'
    return render(request, 'contacts.html', locals())


def galery(request):
    debug = debug_flag
    page = 'galery'
    return render(request, 'galery.html', locals())

# Create your views here.
