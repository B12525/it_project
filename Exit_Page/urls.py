from django.conf.urls import path
from . import views

urlpatterns = [
path('',views.register_name,name = "register_name")
]
