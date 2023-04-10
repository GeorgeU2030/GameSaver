from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.screeninit),
    path('login/home',views.showhome,name='home'),
    path('addgame',views.showaddgame),
    path('newgame',views.newgame)
]