from django.urls import path
from . import views

urlpatterns =[
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("account-settings/", views.account_settings, name="account-settings"),
    path("account/", views.account, name="account"),
    path("edit/<int:id>/", views.edit, name="edit"),
]