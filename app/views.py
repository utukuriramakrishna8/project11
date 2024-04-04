from django.shortcuts import render

def conditions(request):
    d={'a':10,'b':20}
    return render(request,'conditions.html',d)
def nestedif(request):
    d={'a':400,'b':300,'c':200}
    return render(request,'nestedif.html',d)
def loop(request):
    d={'name':'krishna'}
    return render(request,'loop.html',d)
# Create your views here.
