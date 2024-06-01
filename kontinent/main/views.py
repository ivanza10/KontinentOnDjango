from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
def onas(request):
    return render(request, 'main/onas.html')
def kontakt(request):
    return render(request, 'main/kontakt.html')
def chaikovskiy(request):
    return render(request, 'main/chaikovskiy.html')
def slavniy(request):
    return render(request, 'main/slavniy.html')
def grani(request):
    return render(request, 'main/grani.html')