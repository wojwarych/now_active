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
    path('', HomeView.as_view(extra_context={'title': 'Home'})),
    path('upcoming_classes/',
         UpcomingClasses.as_view(extra_context={'title': 'Upcoming Classes'}),
         name="upcoming-classes"),
    path('additional_attendance/',
         AdditionalAttendance.as_view(
                            extra_context={'title': 'Additional Attendance'}),
         name="additional-attendance"),
    path('settlements/',
         Settlements.as_view(extra_context={'title': 'Settlements'}),
         name="settlements"),
    path('signups/',
         SignupClass.as_view(extra_context={'title': 'Signup Class'}),
         name="signups"),
    path('personal_detail/',
         PersonalDetail.as_view(extra_context={'title': 'Personal Details'}),
         name="personal-detail")
]
