from django.shortcuts import render

def home(request):              #func name can be anything
    return render(request, 'index.html')
