from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login, get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.conf import settings
from .models import *


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class register_source(forms.ModelForm):

	source = forms.CharField(
		label='Source',
		help_text='Enter source name',
		widget=forms.TextInput(
				attrs={
					'class':'form-control',
				}
		),
		required=False,
	)

	class Meta:
		model = Source
		fields = [
			'source',

		]




class register_url_form(forms.ModelForm):
	source = forms.ModelChoiceField(
		label='Source',
		help_text='URL Source.',
		queryset=Source.objects.all(),
		required=False,
		empty_label=None,
		widget=forms.Select(
			attrs={
				'class':'form-control'
			}
		)
	)

	url = forms.CharField(
		label='URL',
		help_text='Enter the URL without the http: //',
		widget=forms.TextInput(
				attrs={
					'class':'form-control',
				}
		),
		required=False,
	)

	status = forms.BooleanField(
		label='Active',
		help_text='Check the box if the site is active.',
		required=False,
		initial=True
	)

	categorie = forms.ModelChoiceField(
		label='Categorie',
		help_text='Enter the category of the site.',
		queryset=NameCategories.objects.all(),
		required=False,
		empty_label=None,
		widget=forms.Select(
			attrs={
				'class':'form-control'
			}
		)
	)

	company = forms.ModelMultipleChoiceField(
		queryset=CompanyTerm.objects.all(),
		required=False,
		widget=FilteredSelectMultiple("Company", is_stacked=False,  attrs={'class':'form-control'}),
		help_text='Select if you have seen any of these companies mentioned on the site you are about to register.',
	)

	class Meta:
		model = UrlOnion
		fields = [
			'source',
			'url',
			'status',
			'categorie',
			'company',

		]


class NameCategoriesForm(forms.ModelForm):

	categorie = forms.CharField(
		label='Category',
		help_text='Enter a name for the category.',
		widget=forms.TextInput(
				attrs={
					'onkeydown':'Change("id_slug")',
					'class':'form-control',
				}
		),
		required=False,
	)


	class Meta:
		model = NameCategories
		fields = [
			'categorie',

		]


class CategoriesForm(forms.ModelForm):

	categorie = forms.ModelChoiceField(
		label='Category',
		help_text='Select the category for the term.',
		queryset=NameCategories.objects.all(),
		required=False,
		empty_label=None,
		widget=forms.Select(
			attrs={
				'class':'form-control'
			}
		)
	)

	term = forms.CharField(
		label='Term',
		help_text='Please provide a term for the category..',
		widget=forms.TextInput(
				attrs={
					'onkeydown':'Change("id_slug")',
					'class':'form-control',
				}
		),
		required=False,
	)


	class Meta:
		model = Categories
		fields = [
			'categorie',
			'term'

		]


class CompanyNameForm(forms.ModelForm):

	name = forms.CharField(
		label='Company Name',
		help_text='Enter the name of the company you want to register.',
		widget=forms.TextInput(
				attrs={
					'onkeydown':'Change("id_slug")',
					'class':'form-control',
				}
		),
		required=False,
	)


	class Meta:
		model = CompanyName
		fields = [
			'name',

		]


class CompanyTermForm(forms.ModelForm):

	name = forms.ModelChoiceField(
		label='Company',
		help_text='Select the company that will receive the keyword.',
		queryset=CompanyName.objects.all(),
		required=False,
		empty_label=None,
		widget=forms.Select(
			attrs={
				'class':'form-control'
			}
		)
	)

	term = forms.CharField(
		label='Keyword',
		help_text='Enter the keyword.',
		widget=forms.TextInput(
				attrs={
					'onkeydown':'Change("id_slug")',
					'class':'form-control',
				}
		),
		required=False,
	)


	class Meta:
		model = CompanyTerm
		fields = [
			'name',
			'term'

		]


class register_user_form(forms.ModelForm):
	username = forms.CharField(
		label='Username',
		help_text='User that will be used to login to the system, only letters and numbers.',
		widget=forms.TextInput(
				attrs={
					'class':'form-control'
				}
		),
		required=False,
	)
	password1 = forms.CharField(
		label='Password',
		help_text='Enter a password so that it can be used in accessing the system.',
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control'
			}
		)
	)
	password2 = forms.CharField(
		label='Password Confirmation',
		help_text='Confirm the password you entered.',
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control'
			}
		)
	)
	email = forms.EmailField(
		label='E-mail',
		help_text='Enter an E-mail address.',
		widget=forms.EmailInput(
				attrs={
					'class':'form-control',
				}
		),
		required=False,
	)
	name = forms.CharField(
		label='Full Name',
		help_text='Enter your full name.',
		widget=forms.TextInput(
				attrs={
					'class':'form-control',
				}
		),
		required=False,
	)

	is_staff = forms.BooleanField(
		label='Is Staff',
		help_text='Will you be a system administrator user?',
		required=False
	)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Confirmation is not correct.')
		return password2

	def save(self, commit=True):
		user = super(register_user_form, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


	class Meta:
		model = CustomUser
		fields = [
			'username',
			'password1',
			'password2',
			'email',
			'name',


		]

#.Form edit user form
# Criar formulário de edição do usuário

class edit_user_form(forms.ModelForm):
	username = forms.CharField(
		label='Username',
		help_text='User that will be used to login to the system, only letters and numbers.',
		widget=forms.TextInput(
				attrs={
					'class':'form-control',
					'readonly': 'readonly'
				}
		),
		required=False,
	)

	email = forms.EmailField(
		label='E-mail',
		help_text='Enter an Email Address.',
		widget=forms.EmailInput(
				attrs={
					'class':'form-control',
				}
		),
		required=False,
	)
	name = forms.CharField(
		label='Full name',
		help_text='Enter your full name',
		widget=forms.TextInput(
				attrs={
					'class':'form-control',
				}
		),
		required=False,
	)

	is_staff = forms.BooleanField(
		label='Is Staff',
		help_text='Will you be a system administrator user?',
		required=False
	)


	class Meta:
		model = CustomUser
		fields = [
			'username',
			'email',
			'name',


		]
