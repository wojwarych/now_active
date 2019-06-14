from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


# Create your views here.
class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ManagerView(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "manager/manager.html"
