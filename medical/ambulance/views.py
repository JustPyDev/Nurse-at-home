from django.shortcuts import render, redirect

from .forms import UsersForm, FollowForm
from .models import *


# Create your views here.

def index(requests):
    ser = Services.objects.all()
    basic = Basic.objects.all()
    about_us = Office.objects.all()
    nurse = Nurse.objects.all()
    doctor = Doctor.objects.all()
    user = Users.objects.all()
    menu = Menu.objects.all()
    data = Contact.objects.all()
    nurse_value = len(nurse)
    doctor_value = len(doctor)
    menu_value = len(menu)
    user_value = len(user)
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {
        'ser': ser,
        'data': data,
        'nurse_value': nurse_value,
        'doctor_value': doctor_value,
        'menu_value': menu_value,
        'user_value': user_value,
        'basic': basic,
        'about_us': about_us,
    }
    return render(requests, 'index.html', ctx)


def services(requests, slug=None):
    ser_pk = Services.objects.get(slug=slug)
    service = Menu.objects.all().filter(services_id=ser_pk.id)
    ser = Services.objects.all()
    plus = Service.objects.all()
    data = Contact.objects.all()
    about_us = Office.objects.all()
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')

    ctx = {
        'ser': ser,
        'ser_pk': ser_pk,
        'service': service,
        'data': data,
        'about_us': about_us,
        'plus': plus
    }
    return render(requests, 'services.html', ctx)


def about(requests):
    nurse = Nurse.objects.all()
    doctor = Doctor.objects.all()
    user = Users.objects.all()
    menu = Menu.objects.all()
    ser = Services.objects.all()
    data = Contact.objects.all()
    about_us = Office.objects.all()
    about_ser = About_us.objects.all()
    nurse_value = len(nurse)
    doctor_value = len(doctor)
    menu_value = len(menu)
    user_value = len(user)
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {
        'data': data,
        'ser': ser,
        'nurse_value': nurse_value,
        'doctor_value': doctor_value,
        'menu_value': menu_value,
        'user_value': user_value,
        'about_us': about_us,
        'about_ser': about_ser
    }
    return render(requests, 'about-us.html', ctx)


def contact(requests):
    ser = Services.objects.all()
    data = Contact.objects.all()
    about_us = Office.objects.all()
    basic = data[0]
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {
        'data': data,
        'ser': ser,
        'basic': basic,
        'about_us': about_us
    }
    return render(requests, 'contact.html', ctx)


def services_menu(requests, slug=None):
    ser_pk = Menu.objects.get(slug=slug)
    service = Tariffs.objects.all().filter(services_id=ser_pk.id)
    ser = Services.objects.all()
    data = Contact.objects.all()
    about_us = Office.objects.all()
    plus = Service.objects.all()
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {
        'ser_pk': ser_pk,
        'service': service,
        'data': data,
        'ser': ser,
        'about_us': about_us,
        'plus': plus
    }
    return render(requests, 'services_menu.html', ctx)


def all_services(requests, slug=None):
    ser_pk = Menu.objects.all()
    ser = Services.objects.all()
    data = Contact.objects.all()
    about_us = Office.objects.all()
    plus = Service.objects.all()
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')

    ctx = {
        'ser_pk': ser_pk,
        'data': data,
        'ser': ser,
        'about_us': about_us,
        'plus': plus
    }
    return render(requests, 'all_services.html', ctx)


def servicess(requests, pk=None):
    ser_pk = Tariffs.objects.get(pk=pk)
    ser = Services.objects.all()
    basic = Basic.objects.all()
    about_us = Office.objects.all()
    data = Contact.objects.all()
    plus = Service.objects.all()
    form = UsersForm()
    if requests.POST:
        forms = FollowForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    if requests.POST:
        forms = UsersForm(requests.POST or None,
                          requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Users.objects.get(pk=root.id)
            root.services = ser_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ser_pk': ser_pk,
        'form': form,
        'data': data,
        'ser': ser,
        'about_us': about_us,
        'plus': plus,
        'basic': basic,
    }
    return render(requests, 'servicespk.html', ctx)


def ctg_list(requests):
    all = Users.objects.all()
    followers = Follower.objects.all()
    all_f1 = followers[::-1]
    all_f2 = followers[::-1][1]
    all_f3 = followers[::-1][2]
    all_f4 = followers[::-1][3]
    all_f5 = followers[::-1][4]
    all1 = all[::-1]
    all2 = all[::-1][1]
    all3 = all[::-1][2]
    all4 = all[::-1][3]
    all5 = all[::-1][4]
    ctx = {
        "all": all,
        "all1": all1,
        "all2": all2,
        "all3": all3,
        "all4": all4,
        "all5": all5,
        'all_f1': all_f1,
        'all_f2': all_f2,
        'all_f3': all_f3,
        'all_f4': all_f4,
        'all_f5': all_f5,
    }
    return render(requests, 'list.html', ctx)
