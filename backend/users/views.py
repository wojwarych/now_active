from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView
from django.views.generic import FormView

from utils.extra_context import ExtraContext


# Create your views here.
class SignInView(ExtraContext, FormView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "forms/signin.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        self.success_url = ("/manager/"
                            if form.get_user().is_staff
                            else "/home/")
        return super(SignInView, self).form_valid(form)


class SignOutView(ExtraContext, RedirectView):
    url = "/signin/"

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)
