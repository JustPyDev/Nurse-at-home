from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('User_follower_list/', views.ctg_list, name='ctg_list'),
    path("services/<slug>/", views.services, name='ser_one'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('all_services/', views.all_services, name="all_services"),
    path('servicess/<int:pk>/', views.servicess, name="servic_one"),
    path('services_menu/<slug>/', views.services_menu, name="ser_menu_one"),
]