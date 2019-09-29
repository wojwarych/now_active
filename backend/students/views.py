from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from utils.extra_context import ExtraContext


# Create your views here.
class HomeView(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/home.html"

    def get(self, request, *args, **kwargs):
        return redirect("upcoming-classes")


class UpcomingClasses(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/upcoming_classes.html"


class AdditionalAttendance(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/additional_attendance.html"


class Settlements(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/settlements.html"


class SignupClass(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/signup_class.html"


class PersonalDetail(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/personal_detail.html"
