from django.urls import path, include
from django.conf.urls import handler404
from . import views


urlpatterns = [
    path('', views.IndexTemplate.as_view(), name='index'),
    path('representante_legal_create/', views.RepresentanteLegalCreateView.as_view(), name='representante_legal_create'),
    path('representante_legal_list/', views.RepresentanteLegalListView.as_view(), name='representante_legal_list'),
    path('representante_legal_update/<int:pk>/', views.RepresentanteLegalUpdateView.as_view(), name='representante_legal_update'),
    path('representante_legal_detail/<int:pk>/', views.RepresentanteLegalDetailView.as_view(), name='representante_legal_detail'),
    path('representante_legal_delete/<int:pk>/', views.RepresentanteLegalDeleteView.as_view(), name='representante_legal_delete'),
    ]
