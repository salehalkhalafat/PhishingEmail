from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePage, name='home'),
    path('phishing/', views.phishingPage, name='phishing'),
    path('fetchem/', views.seperate, name='fetch'),
]
