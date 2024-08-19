from django.urls import path

from converter import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resultRus', views.resultRus, name='resultRus'),
    path('Rus', views.Rus, name='Rus'),
    path('resultEng', views.resultEng, name='resultEng'),
]




