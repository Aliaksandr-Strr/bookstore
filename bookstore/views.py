from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Books
from .cron import database_update


class AllBooksView(ListView):
    model = Books
    template_name = 'bookstore/main.html'
    paginate_by = 5


class UsersLoginView(LoginView):
    template_name = 'bookstore/login.html'


class UsersLogoutView(LogoutView):
    next_page = '/'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'bookstore/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)
