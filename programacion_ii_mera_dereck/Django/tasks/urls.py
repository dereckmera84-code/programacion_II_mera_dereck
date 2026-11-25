from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("clubs/", views.club_list, name="clubs"),
]
