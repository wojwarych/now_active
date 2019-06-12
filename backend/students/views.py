from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):

    template_name = "students/home.html"


class UpcomingClasses(TemplateView):

    template_name = "students/upcoming_classes.html"


class AdditionalAttendance(TemplateView):

    template_name = "students/additional_attendance.html"


class Settlements(TemplateView):

    template_name = "students/settlements.html"


class SignupClass(TemplateView):

    template_name = "students/signup_class.html"


class PersonalDetail(TemplateView):

    template_name = "students/personal_detail.html"
