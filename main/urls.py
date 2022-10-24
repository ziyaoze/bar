
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home, name="home"),
path('contact', views.contact, name="contact"),
path('about', views.about, name="about"),
path('barber', views.barber, name="barber"),
path('bookings/<pk>', views.bookings, name="bookings"),
path('appointments', views.appointments, name="appointments"),


path('reject/<pk>', views.delete, name="reject"),


path('open', views.open, name="open"),
path('close', views.close, name="close"),

]
