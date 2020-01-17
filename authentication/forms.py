from django import forms
from authentication.models import Profile


class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'user_type',
            'first_name',
            'last_name',
            'organization',
            'location_city',
            'location_state',
            'terms_agree',
            'main_picture',
        )

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, user):

        # Save your profile
        profile = Profile()
        profile.user = user
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.organization = self.cleaned_data['organization']
        profile.location_city = self.cleaned_data['location_city']
        profile.location_state = self.cleaned_data['location_state']
        #profile.terms_agree = self.cleaned_data['terms_agree']
        profile.main_picture = self.cleaned_data['main_picture']

        # Save your user and profile
        user.save()
        profile.save()
