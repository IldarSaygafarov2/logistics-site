from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_home_page, name="home"),
    path("contact/", views.render_contact_page, name="contact"),
    path("about/", views.render_about_page, name="about"),
    path("send/", views.send_message_to_request, name="send_message"),
    path("find/", views.find_by_track_id, name="find_id"),
]
