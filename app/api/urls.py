from django.urls import path

from files.views import FileView


app_name = "api"

urlpatterns = [
    path("upload/", FileView.as_view({"post": "create"}), name="upload"),
    path("files/", FileView.as_view({"get": "list"}), name="list"),
]