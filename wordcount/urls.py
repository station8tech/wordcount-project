
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutPage/', views.about, name='about'),
    path('counting/', views.count, name='count')
]
