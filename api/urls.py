from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping_view,name='ping'),
    path('posts/', views.post_view,name='posts'),  
]