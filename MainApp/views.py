from django.shortcuts import render

debug = True

def main(request):
    page = 'index'
    return render(request, 'index.html', {"page": page, "debug": debug})

def about(request):
    page = 'about'
    return render(request, 'about.html', {"page": page, "debug": debug})

def photograph(request):
    page = 'photograph'
    return render(request, 'photograph.html', {"page": page, "debug": debug})

def photographs(request):
    page = 'photographs'
    # Временно отрисовывается персональная страница фотографа
    return render(request, 'photograph.html', {"page": page, "debug": debug})

# Create your views here.
