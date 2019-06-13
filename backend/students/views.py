from django.shortcuts import redirect
from django.views.generic.base import TemplateView


# Create your views here.
class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class HomeView(ExtraContext, TemplateView):

    template_name = "students/home.html"

    def get(self, request, *args, **kwargs):
        return redirect("upcoming-classes")


class UpcomingClasses(ExtraContext, TemplateView):

    template_name = "students/upcoming_classes.html"


class AdditionalAttendance(ExtraContext, TemplateView):

    template_name = "students/additional_attendance.html"


class Settlements(ExtraContext, TemplateView):

    template_name = "students/settlements.html"


class SignupClass(ExtraContext, TemplateView):

    template_name = "students/signup_class.html"


class PersonalDetail(ExtraContext, TemplateView):

    template_name = "students/personal_detail.html"
