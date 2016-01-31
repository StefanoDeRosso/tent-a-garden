from django import forms
from django.forms import ModelForm, Textarea
from tentagarden.models import UserProfile
from django.contrib.auth.models import User
from parsley.decorators import parsleyfy
from django.utils.translation import ugettext_lazy as _

class FileForm(forms.Form):
	docfile = forms.FileField(
		label='Select a file',
		help_text='max. 42 megabytes'
	)


@parsleyfy
class UserForm(forms.ModelForm):
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs = {
            'placeholder': 'Password',
			'class': 'form-control'
        }))
        
	first_name = forms.CharField(label='', required=True, widget = forms.TextInput(
        attrs = {
            'placeholder': 'First name',
			'class': 'form-control'
        }
    ))
    
	last_name = forms.CharField(label='', required=True, widget = forms.TextInput(
        attrs = {
            'placeholder': 'Last name',
			'class': 'form-control'
        }
    ))
    
	email = forms.CharField(label='', required=True, widget = forms.EmailInput(
        attrs = {
            'placeholder': 'E-Mail',
			'class': 'form-control'
        }
    ))
    
	username = forms.CharField(label='', required=True, widget = forms.TextInput(
        attrs = {
            'placeholder': 'Username',
			'class': 'form-control'
        }
    ))
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')
		#labels = {
        #    'username': _("")
        #}
        #help_texts = {
        #    'username': _('Some useful help text.'),
        #}
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')
		labels = {
            'website': _(""),
            'picture': _(""),
        }
