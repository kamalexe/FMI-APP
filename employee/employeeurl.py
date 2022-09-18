from django.urls import path
from . import views

urlpatterns = [
    path('', views.emphome, name='emphome'),
    path('reg/', views.reg, name='reg'),
    path('insert/', views.insert, name='insert'),
]