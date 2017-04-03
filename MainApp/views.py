from django.shortcuts import render

def main(request):
    page = 'index'
    debug = True
    return render(request, 'index.html', {"page": page, "debug": debug})

# Create your views here.
