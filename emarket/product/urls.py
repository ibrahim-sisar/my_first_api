from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_all),
    path('single/<pk>/',views.single_obj),
    path('single2/<text>/',views.search),
   
]