from django.urls import path
from . import views

# BELOW URL ASSIGNED AND INCLUDE THE VIEW FUNCTION

urlpatterns = [
    path('', views.home, name="home page"),

]
