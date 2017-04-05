from django.shortcuts import render

debug = True

def main(request):
    page = 'index'
    return render(request, 'index.html', {"page": page, "debug": debug})

# Create your views here.
