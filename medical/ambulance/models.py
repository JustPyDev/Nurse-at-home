from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Services(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    slug = models.SlugField(verbose_name=_('slug'), unique=True, max_length=156, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    slug = models.SlugField(verbose_name=_('slug'), unique=True, max_length=156, blank=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    character = models.TextField(verbose_name=_('character'))

    def __str__(self):
        return self.name


class Follower(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=256)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(verbose_name=_('phone_number'), max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Tariffs(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=256)
    slug = models.SlugField(verbose_name=_('slug'), unique=True, max_length=156, blank=True)
    price = models.IntegerField(verbose_name=_('price'))
    type_price = models.CharField(verbose_name=_('type_price'), max_length=156)
    services = models.ForeignKey(Menu, on_delete=models.CASCADE)
    character = models.TextField(verbose_name=_('character'))

    def __str__(self):
        return self.name


class Basic(models.Model):
    name_services = models.CharField(verbose_name=_('name_services'), max_length=255)
    about_services = models.TextField(verbose_name=_('about_services'))
    name_nurses = models.CharField(verbose_name=_('name_nurses'), max_length=255)
    about_nurses = models.CharField(verbose_name=_('about_nurses'), max_length=400)
    name_search = models.CharField(verbose_name=_('name_search'), max_length=255)
    about_search = models.CharField(verbose_name=_('about_search'), max_length=400)
    name_choose = models.CharField(verbose_name=_('name_choose'), max_length=255)
    choose_us = models.TextField(verbose_name=_('choose_us'))
    image = models.ImageField(verbose_name=_('image'))

    def __str__(self):
        return self.name_services


class About_us(models.Model):
    name_header = models.CharField(verbose_name=_('name_header'), max_length=255)
    about_header = models.TextField(verbose_name=_('about_header'))
    image_header = models.ImageField(verbose_name=_('image_header'))
    name_footer = models.CharField(verbose_name=_('name_footer'), max_length=255)
    about_footer = models.TextField(verbose_name=_('about_footer'))
    image_footer = models.ImageField(verbose_name=_('image_footer'))

    def __str__(self):
        return self.name_header


class Office(models.Model):
    working_time = models.CharField(verbose_name=_('working_time'), max_length=255)
    city = models.CharField(verbose_name=_('city'), max_length=255, null=True)
    address = models.CharField(verbose_name=_('address'), max_length=255)
    phone_number = models.CharField(verbose_name=_('phone_number'), max_length=100)
    email = models.EmailField(blank=True)
    emergency_number = models.CharField(verbose_name=_('emergency_number'), max_length=100)
    about_site = models.CharField(verbose_name=_('about_site'), max_length=400, null=True)

    def __str__(self):
        return self.city


class Service(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    character = models.TextField(verbose_name=_('character'))
    image = models.ImageField(verbose_name=_('image'))

    def __str__(self):
        return self.name


class Contact(models.Model):
    working_time = models.CharField(verbose_name=_('working_time'), max_length=255)
    city = models.CharField(verbose_name=_('city'), max_length=255, null=True)
    address = models.CharField(verbose_name=_('address'), max_length=255)
    phone_number = models.CharField(verbose_name=_('phone_number'), max_length=100)
    email = models.EmailField(blank=True)
    emergency_number = models.CharField(verbose_name=_('emergency_number'), max_length=100)
    about_site = models.CharField(verbose_name=_('about_site'), max_length=400, null=True)

    def __str__(self):
        return self.city


class Users(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    number = models.CharField(verbose_name=_('number'), max_length=255)
    map = models.TextField(verbose_name=_('map'), max_length=255)
    services = models.ForeignKey(Tariffs, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Nurse(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=255)
    age = models.IntegerField(verbose_name=_('age'))
    number = models.CharField(verbose_name=_('number'), max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=255)
    age = models.IntegerField(verbose_name=_('age'))
    number = models.CharField(verbose_name=_('number'), max_length=255)

    def __str__(self):
        return self.name