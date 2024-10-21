from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello', views.hello),
    path('', views.home),
    path('task', views.task),
    path('all-analytics', views.analytics),
    # path('<slug:shorturl>', views.redirect_url),

]