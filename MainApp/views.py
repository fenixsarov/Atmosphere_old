from django.shortcuts import render

def main(request):
    page = 'index'
    return render(request, 'index.html', {"page": page})

# Create your views here.
