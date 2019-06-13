from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView
from django.views.generic.base import TemplateView


# Create your views here.
class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


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


class SignInView(ExtraContext, FormView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "students/signin_form.html"
    form_class = AuthenticationForm
    success_url = '/home/'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(SignInView, self).form_valid(form)


class SignOutView(ExtraContext, RedirectView):
    url = "/signin/"

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)
