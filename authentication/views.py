import os

from django.shortcuts import render, redirect

from django.core.mail import send_mail

from django.views.generic import View, FormView, TemplateView, DetailView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
 
from .forms import UserSignUp

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'ui/dashboard.html'

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

            return redirect('/dashboard')

        else:
            return render(request, 'signup.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })


# class Login(FormView):
#     template_name = "login.html"
#     form_class = AuthenticationForm
#     success_url = "/dashboard/"

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             user = form.get_user()
#             login(self.request, user)
#             return redirect(self.get_success_url())
#         else:
#             return self.form_invalid(form)


# class Logout(FormView):

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect("/")
