from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
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


class StudentCreate(LoginRequiredMixin, ExtraContext, CreateView):
    model = User
    fields = ['username', 'phone_number']
    template_name = "forms/student_create.html"
    success_url = '/manager/'

    def form_valid(self, form, *args, **kwargs):
        response = super(StudentCreate, self).form_valid(form)
        password = User.objects.make_random_password(length=10)
        self.object.set_password(password)
        self.object.email = self.object.username
        self.object.save()
        send_mail(
            'Created your account!',
            f'Your temporary password is: f{password}',
            'from@example.com',
            [f'{self.object.email}'],
        )
        return response
