from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.mi_vista, name="mivista"),
]