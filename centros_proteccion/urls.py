from django.urls import path, include
from django.conf.urls import handler404
from . import views

handler404 = views.custom_404

urlpatterns = [
    path('', views.IndexTemplate.as_view(), name='index'),
    path('representante_legal_create/', views.RepresentanteLegalCreateView.as_view(), name='representante_legal_create'),
    path('representante_legal_list/', views.RepresentanteLegalListView.as_view(), name='representante_legal_list'),
    ]
