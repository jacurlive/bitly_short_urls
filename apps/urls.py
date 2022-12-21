from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from apps.views import MainFormView, ShortView, CustomLoginView, RegistrationView

urlpatterns = [
    path('', MainFormView.as_view(), name='main'),
    path('signup', RegistrationView.as_view(), name='signup'),
    path('signin', CustomLoginView.as_view(), name='sign-in'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('main')), name='logout'),
    path('<str:name>', ShortView.as_view(), name='short_view'),
]
