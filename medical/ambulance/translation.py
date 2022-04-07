from modeltranslation.translator import register, TranslationOptions
from .models import Services, Menu, Tariffs, Contact, Basic, About_us, Office, Service, Follower


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name', 'character')


@register(Tariffs)
class TariffsTranslationOptions(TranslationOptions):
    fields = ('name', 'type_price', 'character')


@register(Basic)
class BasicTranslationOptions(TranslationOptions):
    fields = ('name_services', 'about_services', 'name_nurses', 'about_nurses',
              'name_search', 'about_search', 'name_choose', 'choose_us')


@register(About_us)
class About_usTranslationOptions(TranslationOptions):
    fields = ('name_header', 'about_header', 'name_footer', 'about_footer')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('working_time', 'city', 'address', 'about_site')


@register(Office)
class OfficeTranslationOptions(TranslationOptions):
    fields = ('working_time', 'city', 'address', 'about_site')


@register(Service)
class OfficeTranslationOptions(TranslationOptions):
    fields = ('name', 'character')

