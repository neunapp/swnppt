from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

#import forms
from .forms import UserAddForm, UserLoginForm



class UserAddView(CreateView):
    """
    vista que crea usuarios
    """

    form_class = UserAddForm
    template_name = 'home/registration.html'
    success_url = '.'

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        user = form.save(commit=False)
        email    = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.username = email
        user.set_password(password)
        user.save()
        return super(UserAddView, self).form_valid(form)



class UserLoginView(FormView):
    """ View para logear usuario """

    template_name = 'home/login.html'
    success_url = '.'
    form_class = UserLoginForm

    def form_valid(self, form):

        # Verfiamos si el usuario y contrasenha son correctos.
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(
                    reverse(
                        'home_app:home-contactus'
                    )
                )
            else:
                return HttpResponseRedirect(
                    reverse(
                        'users_app:user-login'
                    )
                )


class LogoutView(View):
    """
    cerrar sesion
    """
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

