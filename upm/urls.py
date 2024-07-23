from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("project", views.project, name="project"),
    path("service", views.service, name="service"),
    path("team", views.team, name="team"),
    path("404", views.r404, name="404"),
]
