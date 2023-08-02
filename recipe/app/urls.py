from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:id>', views.details, name="detail"),
    path('create/', views.create, name="create"),
    path('account/', views.account_page, name="account"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('seach_recipe/', views.search_recipe, name="search"),
    path('profile/<int:id>/', views.profile, name="profile")
]