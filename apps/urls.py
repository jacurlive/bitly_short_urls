from django.urls import path

from apps.views import MainFormView, ShortView

urlpatterns = [
    path('', MainFormView.as_view(), name='form_view'),
    path('<str:name>', ShortView.as_view(), name='short_view'),
]
