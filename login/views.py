from django.shortcuts import render
from login.models import Games,User

# Create your views here.


def screeninit(request):
    return render(request,'initscreen.html')

def showhome(request):
    userid = request.user.id
    games = Games.objects.filter(user__id=userid)
    data = {'games':games}
    return render(request,'home.html',data)

def showaddgame(request):
    return render(request,'addgame.html')

def newgame(request):
    if request.method=='POST':
        usercurrent = request.user.id
        namegame = request.POST['namegame'] 
        yeargame = request.POST['year']
        pricegame = request.POST['price']
        try:
            picture = request.FILES['txtfot']
        except:
            picture = "users/profile_default.png"

        storagegame = request.POST['storage']
        scoregame = request.POST['inpscore']
        platgame = ""
        xboxplat=""
        psplat=""
        ninplat=""
        try:
            xboxplat = request.POST['xboxbtn'] 
        except:
            print('error')
        try:
            psplat = request.POST['inpplay'] 
        except:
            print('error')
        try:
            ninplat = request.POST['btnnin']
        except:
            print('error')
        platgame = xboxplat+psplat+ninplat
        rt=""
        r1=""
        r2=""
        r3=""
        r4=""
        r5=""

        try:
            r1 = request.POST['ebtn']
        except:
            print('error')
        try:
            r2 = request.POST['e10btn']
        except:
            print('error')
        try:
            r3 = request.POST['tbtn']
        except:
            print('error')
        try:
            r4 = request.POST['mbtn']
        except:
            print('error')
        try:
            r5 = request.POST['abtn']
        except:
            print('error')

        rt=r1+r2+r3+r4+r5

        usergame = User.objects.get(id=usercurrent)
        game = Games(name=namegame,year=yeargame,prize=pricegame,image=picture,storage=storagegame,score=scoregame,
                     platform=platgame,rating=rt,user=usergame)

        game.save()
        userid = request.user.id
        games = Games.objects.filter(user__id=userid)
        data = {'games':games}
        
        return render(request,"home.html",data)