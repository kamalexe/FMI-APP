from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('smRegView', views.smRegView, name='smRegView'),
    path('smReg', views.smReg, name='smReg'),
    path('smLoginView', views.smLoginView, name='smLoginView'),
    path('smLogin', views.smLogin, name='smLogin'),
    path('smProfile', views.smProfile, name='smProfile'),
]