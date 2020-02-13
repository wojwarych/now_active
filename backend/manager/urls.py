from django.urls import path

from .views import (
    GroupsList,
    ManagerView,
    StudentCreate,
    StudentsList,
    TrainersList,
)


urlpatterns = [
    path('', ManagerView.as_view(extra_context={'title': 'Manager'})),
    path('students', StudentsList.as_view(
        extra_context={'title': 'Students'}),
        name="students-list"),
    path('trainers', TrainersList.as_view(
        extra_context={'title': 'Trainers'}),
        name="trainers-list"),
    path("groups", GroupsList.as_view(
        extra_context={"title": "Groups"}),
        name="groups-list",
    ),
    path("student-add", StudentCreate.as_view(), name="student-add"),
]
