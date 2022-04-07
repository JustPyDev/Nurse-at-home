from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.
@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Menu)
class MenuAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tariffs)
class TariffsAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Basic)
class BasicAdmin(TranslationAdmin):
    pass


@admin.register(About_us)
class About_usAdmin(TranslationAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    pass


@admin.register(Office)
class OfficeAdmin(TranslationAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    pass


admin.site.register(Follower)
admin.site.register(Nurse)
admin.site.register(Doctor)
admin.site.register(Users)


