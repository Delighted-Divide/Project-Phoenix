from django.urls import path
from . import views


urlpatterns = [
    path('<str:uname>/', views.log, name="Login"),
]
