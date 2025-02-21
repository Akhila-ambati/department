

from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('add/', views.department_add, name='department_add'),
    path('edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('delete/<int:pk>/', views.department_delete, name='department_delete'),
    path('view/<int:pk>/', views.department_view, name='department_view'),  # New URL for View
]