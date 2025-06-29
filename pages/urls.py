# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crear/', views.page_create, name='page_create'),
    path('editar/<slug:slug>/', views.page_edit, name='page_edit'),
    path('eliminar/<slug:slug>/', views.page_delete, name='page_delete'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),  # ¡Esto va al final!
]
