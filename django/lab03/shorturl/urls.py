from django.urls import path
from . import views


urlpatterns = [
        path('', views.short_url, name='short_url'),
        path('<str:short_url>/', views.url_redirect, name='url_redirect'),

]
