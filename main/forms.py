from django import forms
from .models import FeedBackRequest


class RequestForm(forms.ModelForm):
	class Meta:
		model = FeedBackRequest

		fields = (
			'name',
			'email',
			'phone',
			'additional_message',
		)
		
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Name Last Name'}),
			'email': forms.TextInput(attrs={'placeholder': 'Email'}),
			'phone': forms.TextInput(attrs={'placeholder': '+0 (000) 0000 00'}),
			"additional_message": forms.Textarea(attrs={'placeholder': 'Additional message. (not required)'}),
		}

	def __init__(self, *args, **kwargs):		
		super().__init__(*args, **kwargs)

		self.fields["name"].label = ''
		self.fields["email"].label = ''
		self.fields["phone"].label = ''
		self.fields["additional_message"].label = ''
		self.fields["additional_message"].required = False
		
		
