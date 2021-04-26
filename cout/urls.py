from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from cout import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name="contact")
]