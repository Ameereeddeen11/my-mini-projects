from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:id>', views.details, name="detail"),
    path('create/', views.create, name="create")
]