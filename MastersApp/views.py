from django.shortcuts import render

debug = True

def Master_Page(request):
    page = 'master_page'
    return render(request, "master_page.html", {"page": page, "debug": debug})

# Create your views here.
