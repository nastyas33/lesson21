from django.urls import path
from .views import TaskListView
from .services import add_item, delete_item


urlpatterns = [
    path("", TaskListView.as_view()),
    path("add/", add_item),
    path("delete/<int:object>", delete_item)
]