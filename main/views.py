from django.shortcuts import render, redirect, reverse
from .models import Booking, Shop
from datetime import date, datetime, time
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context = {}
    shop= Shop.objects.get(id=1)
    context['shop'] = shop

    booking = Booking.objects.all().count()
    context['reservations'] = booking


    return render(request, 'home.html', context)
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def bookings(request, pk):
    barbers=User.objects.all()
    context={
        'barbers':barbers
    }
    if request.method == "POST":
        name=request.POST.get('name')

        barberss=User.objects.get(id=pk)

        data = Booking()
        data.name= name
        data.barber=barberss

        data.save()

        return redirect('home')
    return render(request, 'bookings.html', context)
def barber(request):
    barbers=User.objects.all()
    context={
        'barbers':barbers
    }



    return render(request, 'barber.html', context)


@login_required
def appointments(request):
    total=Booking.objects.filter(barber=request.user).count()


    appointments=Booking.objects.all()
    context={
        'appointments':appointments,
        'shop':Shop.objects.get(id=1),
        'total':total,
    }

    return render(request, 'appointments.html', context)

@login_required
def delete(request, pk):
    appointments=Booking.objects.get(id=pk)
    id=appointments.id
    if request.method == "POST":
        appointments.delete()
        return redirect('appointments')


def close(request):
    context = {}
    shop, created = Shop.objects.get_or_create(id=1)
    context['shop'] = shop
    if request.method=='POST':
        shop.status=False
        shop.save()
        return redirect('appointments')

def open(request):
    context = {}
    shop, created = Shop.objects.get_or_create(id=1)
    context['shop'] = shop
    if request.method=='POST':
        shop.status=True
        shop.save()
        return redirect('appointments')



