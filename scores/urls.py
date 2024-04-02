from django.urls import path
from scores import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fixtures/', views.fixtures, name='fixtures'),
]