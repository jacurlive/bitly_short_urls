from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from apps.forms import UrlForm, CustomLoginForm, RegisterForm
from apps.models import Url, User


class MainFormView(FormView):
    form_class = UrlForm
    template_name = 'apps/index.html'
    success_url = reverse_lazy('main_view')

    def form_valid(self, form):
        url = form.save()
        url = f'{url.short_name}'
        context = {
            'short_name': url,
            'user_count': User.objects.count(),
            'link_count': Url.objects.count()
        }
        return render(self.request, 'apps/index.html', context)


class ShortView(View):

    def get(self, request, name, *args, **kwargs):
        url = Url.objects.get(short_name=name)
        return HttpResponseRedirect(url.long_name)


class CustomLoginView(LoginView):
    template_name = 'apps/sign-in.html'
    form_class = CustomLoginForm
    next_page = reverse_lazy('main')


class RegistrationView(FormView):
    form_class = RegisterForm
    template_name = 'apps/sign-up.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

