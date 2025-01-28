from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduction/', views.intro, name='intro'),
    path('composition/', views.tea_view, name='tea_view'),
    path('fertilizers/', views.chemicals, name='chemicals'),
    path('practices/', views.best_practice, name='best_practice'),
    path('predict_sickness/', views.predict_sickness, name='predict_sickness'),
]
