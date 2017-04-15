from django.shortcuts import render

debug = True

def main(request):
    page = 'index'
    return render(request, 'index.html', {"page": page, "debug": debug})

def about(req):
    page = 'about'
    return render(req, 'about.html', {"page": page, "debug": debug})

def photograph(req):
    page = 'photograph'
    return render(req, 'photograph.html', {"page": page, "debug": debug})


# Create your views here.
