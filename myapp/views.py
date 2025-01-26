from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'introduction.html')

def tea_view(request):
    return render(request, 'composition.html')

def chemicals(request):
    return render(request, 'fertilizers.html')

def best_practice(request):
    return render(request, 'practices.html')