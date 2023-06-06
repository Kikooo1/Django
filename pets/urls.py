from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('species/', views.species_list, name='species_list'),
    path('species/create/', views.species_create, name='species_create'),
    path('species/update/<int:pk>/', views.species_update, name='species_update'),
    path('species/delete/<int:pk>/', views.species_delete, name='species_delete'),

    path('vaccines/', views.vaccines_list, name='vaccines_list'),
    path('vaccines/create/', views.vaccines_create, name='vaccines_create'),
    path('vaccines/update/<int:pk>/', views.vaccines_update, name='vaccines_update'),
    path('vaccines/delete/<int:pk>/', views.vaccines_delete, name='vaccines_delete'),

    path('', views.pet_info_list, name='pet_info_list'),
    path('pets/create/', views.pet_info_create, name='pet_info_create'),
    path('pets/update/<int:pk>/', views.pet_info_update, name='pet_info_update'),
    path('pets/delete/<int:pk>/', views.pet_info_delete, name='pet_info_delete'),

    path('pets/history/create/<int:pk>/', views.history_create, name='history_create'),

    path('pets/vaccines_administered/create/<int:pk>/', views.vaccines_administered_create, name='vaccines_administered_create'),

    path('pets/detail/<int:pk>/', views.pet_info_detail, name='pet_info_detail'),
]

