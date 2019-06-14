from django.urls import path

from .views import ManagerView


urlpatterns = [
    path('', ManagerView.as_view(extra_context={'title': 'Manager'})),
]
