from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.

def webpage1(request):
     reslut= render_to_string("initial/home.html")
     return HttpResponse(reslut)

def webpage2(request):
    return render(request, 'initial/about_us.html')

def webpage3(request):
    return render(request, 'initial/admin.html')

def webpage4(request):
    return render(request, 'initial/buy.html')

def webpage5(request):
    return render(request, 'initial/index.html')

def webpage6(request):
    return render(request, 'initial/login.html')

def webpage7(request):
    return render(request, 'initial/menclothing.html')

def webpage8(request):
    return render(request, 'initial/menshoes.html')

def webpage9(request):
    return render(request, 'initial/menswimware.html')

def webpage10(request):
    return render(request, 'initial/register.html')

def webpage11(request):
    return render(request, 'initial/womenclothing.html')

def webpage12(request):
    return render(request, 'initial/womenshoes.html')

def webpage13(request):
    return render(request, 'initial/womenswimware.html')