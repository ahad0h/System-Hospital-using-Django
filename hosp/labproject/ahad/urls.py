from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('add/', views.add_patient, name='add_patient'),
    path('search/', views.search_patients, name='search_patients'),  # ← الجديد
]
