from django.urls import path

from .views import (
    HomeView,
    UpcomingClasses,
    AdditionalAttendance,
    Settlements,
    SignupClass,
    PersonalDetail,
)

urlpatterns = [
    path('', HomeView.as_view()),
    path('upcoming_classes/', UpcomingClasses.as_view(),
         name="upcoming-classes"),
    path('additional_attendance/', AdditionalAttendance.as_view(),
         name="additional-attendance"),
    path('settlements/', Settlements.as_view(),
         name="settlements"),
    path('signups/', SignupClass.as_view(),
         name="signups"),
    path('personal_detail/', PersonalDetail.as_view(),
         name="personal-detail")
]
