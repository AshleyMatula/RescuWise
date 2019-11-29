from django import forms
from authentication.models import Profile

class UserSignUp(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
			"email",
			"user_type",
		]
		# widgets = {
		# 	'user_type':forms.RadioSelect(),
		# }

	def __init__(self, *args, **kwargs):
		super(UserSignUp, self).__init__(*args, **kwargs)