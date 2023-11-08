from django.urls import path
from . import views  # current app @calc import all class present in views.py



urlpatterns = [
    path('',views.home, name="home")
 
 ]
