from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduction.html', views.intro, name='intro_html'),
    path('composition.html', views.tea_view, name='tea_view'),
    path('fertilizers.html', views.chemicals, name='chemicals'),
    path('practices.html', views.best_practice, name='best_practice'),
]