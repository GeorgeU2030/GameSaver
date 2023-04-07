from django.shortcuts import render

# Create your views here.


def screeninit(request):
    return render(request,'initscreen.html')

def showhome(request):
    user = request.user.id
    data = {'u': user}
    return render(request,'home.html',data)