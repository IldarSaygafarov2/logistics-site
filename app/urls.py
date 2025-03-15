from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_home_page, name="home"),
    path("contact/", views.render_contact_page, name="contact"),
    path("about/", views.render_about_page, name="about"),
    path("services/", views.render_services_page, name="services"),
]
