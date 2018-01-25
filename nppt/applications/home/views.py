from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

#forms
from .forms import ContactUsForm

class ContactUsView(CreateView):
    """vista para ContactUs"""

    form_class = ContactUsForm
    template_name = 'home/contact_us.html'
    success_url ='success'
