from django import forms
from .models import FeedBackRequest, DubaiVisaRequest


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


class RequestSearchForm(forms.Form):
	request = forms.CharField(
		max_length=30, 
		widget=forms.TextInput(
		attrs={'placeholder':'Passport series'}), 
		label='')

	def __init__(self, *args, **kwargs):		
		super().__init__(*args, **kwargs)
		self.fields["request"].label = ''
		
	class Meta:
		widgets = {
			'request': forms.TextInput(attrs={'placeholder': 'Passport series'}),
		}


class DubaiVisaRequestForm(forms.ModelForm):
	class Meta:
		model = DubaiVisaRequest

		fields = (
				'passport_registered_at',
				'now_located_in',		
				'first_name',
				'last_name',
				'visa_duration',
				'passport_series',
				'passport_closure_date',
				'contact_information',
				'passport_open_date'
		)

		widgets = {
			'passport_registered_at': forms.Select(attrs={'placeholder': "My passport from"}),
			'now_located_in': forms.Select(attrs={'placeholder': "I'm in"}),
			'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
			'passport_series': forms.TextInput(attrs={'placeholder': 'Passport series'}),
			'contact_information': forms.Textarea(attrs={'placeholder': 'Leave your contact information'}),
			'passport_closure_date': forms.TextInput(attrs={'placeholder': 'passport closure day', 'type':'date'}),
			'passport_open_date': forms.TextInput(attrs={'placeholder': 'passport getting day', 'type':'date'}),

			
		}


	def __init__(self, *args, **kwargs):		
		super().__init__(*args, **kwargs)

		self.fields['passport_registered_at'].label = ''
		self.fields['now_located_in'].label = ''
		self.fields['first_name'].label = ''
		self.fields['last_name'].label = ''
		self.fields['visa_duration'].label = ''
		self.fields['passport_series'].label = ''
		self.fields['passport_closure_date'].label = ''
		self.fields['contact_information'].label = ''
		self.fields['passport_open_date'].label = ''

		
