from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from verified_email_field.forms import VerifiedEmailField
from django.forms import ModelForm


from .models import UserInfo



class signup_form(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username=forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("This username is already taken !")
        return self.cleaned_data['username']

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match !")


class login_form(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)




class UserInfoModelForm(ModelForm):
    class Meta:
        model = UserInfo
        fields= ['blog_title','blog']
