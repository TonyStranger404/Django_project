from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calorie_counter/', views.calorie_counter, name='calorie_counter'),
    path('about/', views.about, name='about'),
]
