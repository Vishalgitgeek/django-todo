from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.index, name="index"),
    path("update_task/<int:task_id>/", view = views.update_task, name = "update_task"),
    path("delete_task/<int:task_id>/", view = views.delete_task, name = "delete_task"),
]