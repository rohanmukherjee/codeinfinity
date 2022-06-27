from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Code Infinity Admin"
admin.site.site_title = "Code Infinity Admin Portal"
admin.site.index_title = "Welcome to codeinfinity Portal" #username-rohan password-rohan

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('create',views.contact,name="create"),
    path('solve',views.solvepage,name="solvepage"),

]
