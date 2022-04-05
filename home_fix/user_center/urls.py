from django.urls import path
from . import views

app_name = "user_center"

urlpatterns = [
    path("request/", views.request_view, name="request"),
    path("provide/", views.provide_view, name="provide"),
    path("transaction/", views.transaction_view, name="transaction"),
    path("profile/", views.profile_view, name="profile"),
    path("profile_editor/", views.profile_editor_view, name="profile_editor"),
    path("contact/", views.contact_view, name="contact"),
]
