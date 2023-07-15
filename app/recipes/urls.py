from django.urls import path
from . import views

urlpatterns =[
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("account-settings/", views.account_settings, name="accountsettings"),
]