from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from mainapp.forms import SomethingForm


class DummyView(FormView):
    form_class = SomethingForm
    template_name = 'mainapp/index.html'
    success_url = '/dummy/'
