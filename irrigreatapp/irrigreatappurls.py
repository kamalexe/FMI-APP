from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('smRegView', views.smRegView, name='smRegView'),
    path('smReg', views.smReg, name='smReg'),
    path('smLoginView', views.smLoginView, name='smLoginView'),
    path('smLogin', views.smLogin, name='smLogin'),
    path('smProfile', views.smProfile, name='smProfile'),
    path('smLogout', views.smLogout, name='smLogout'),
    path('friendprofile/<str:id>', views.friendprofile, name='friendprofile'),
    path('follow', views.follow, name='follow'),
    path('friendprofile/follow/<str:id>', views.follow, name='follow'),
]