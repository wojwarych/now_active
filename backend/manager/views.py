from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from users.models import User
from utils.extra_context import ExtraContext


# Create your views here.
class ManagerView(LoginRequiredMixin, ExtraContext, TemplateView):
    login_url = "/signin/"
    redirect_field_name = "redirect_to"
    template_name = "manager/manager.html"


class StudentsList(LoginRequiredMixin, ExtraContext, ListView):
    model = User
    paginate_by = 20
    template_name = "manager/user_list.html"
    queryset = User.objects.exclude(is_trainer=True)


class TrainersList(LoginRequiredMixin, ExtraContext, ListView):
    model = User
    paginate_by = 20
    template_name = "manager/user_list.html"
    queryset = User.objects.exclude(is_trainer=False)


class GroupsList(LoginRequiredMixin, ExtraContext, ListView):
    model = Group
    paginate_by = 10
    template_name = "manager/groups.html"
    queryset = Group.objects.all()
