from django.shortcuts import render
from core.models import *


from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from RescuWise.forms import *
from django.views.generic import *
from django.views import View
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import os
from django.core.mail import send_mail
from django.contrib import messages
from datetime import *
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AnimalIndex(ListView):
    model = Animal
    template_name = 'animals.html'

class Home(TemplateView):
    template_name = "index.html"

class DynamicStaticPages(TemplateView):


    def get_template_names(self, **kwargs):

        if self.kwargs.get('template_name'):
            # favicons load first so with out this this dynamic view doesn't work.
            if self.kwargs.get('template_name') == "favicon.ico":
                pass
            else:
                return self.kwargs.get('template_name')
        #if there is no url default it index.html

        return "index.html"



class SignUp(View):

    def get(self, request, *args, **kwargs):
        user_form = UserCreationForm()
        profile_form = UserSignUp()


        return render(request, 'signup.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, *args, **kwargs):
            # load both forms to check validity

        user_form = UserCreationForm(self.request.POST)
        profile_form = UserSignUp(self.request.POST)
        # if both are valid...
        if user_form.is_valid() and profile_form.is_valid():

            # save the user form and log the user in
            # saving triggers the create_user_profile function in the
            # Profile model.
            user = user_form.save(commit=False)
            # user.first_name = profile_form.cleaned_data["first_name"]
            # user.last_name = profile_form.cleaned_data["last_name"]
            user.email = user_form.cleaned_data["username"]
            user.username = user_form.cleaned_data["username"]
            user.save()
            login(request, user)

            # after having created the new row in the Profile model for the new user...
            # re-initiate the profile form with the instance and user_id
            # equal to the current user and save the form
            profile_form = UserSignUp(
                self.request.POST, instance=self.request.user.profile)
            profile = profile_form.save(commit=False)
            profile.user_type = profile_form.cleaned_data["user_type"]
            profile_form.save()

            send_mail(
                'New User has signed up',
                user.first_name + ' ' + user.last_name + ' signed up with the email ' + user.email,
                os.environ.get('EMAIL'),
                [os.environ.get('ADMIN_EMAIL')],
                fail_silently=False,
            )

            return redirect('/edit_profile')

        else:

            return render(request, 'signup.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/edit_profile/"

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class Logout(FormView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_view(request, exception=None):
    return render(request, 'errors/500.html', status=500)


def permission_denied_view(request, exception):
    return render(request, 'errors/403.html', status=403)


def bad_request_view(request, exception):
    return render(request, 'errors/400.html', status=400)



class CreateAnimal(CreateView):
    template_name = "createview.html"
    model = Animal
    fields = ['animal_type','name']
    success_url = 'listanimals'


class ListAnimals(ListView):
    template_name = "listview.html"
    model = Animal
    fields = [
        'animal_type',
        'current_shelter',
        'breed',
        'color',
        'name',]

class CreateShelter(CreateView):
    template_name = "createview.html"
    model = Shelter
    fields = [
        'shelter_name',
        'address',
        'phone',
        'email',
        'website']
    success_url = 'list_inventory'


class ListShelters(ListView):
    template_name = "listview.html"
    model = Shelter
