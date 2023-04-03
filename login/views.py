from django.shortcuts import render

# Create your views here.


def screeninit(request):
    return render(request,'initscreen.html')