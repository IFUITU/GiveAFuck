from .models import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    confirm = forms.CharField(max_length=15, widget=forms.PasswordInput)

    def clean_confirm(self): #only with clean_ you can do some operations!
        if self.cleaned_data['password'] != self.cleaned_data['confirm']:
            print('Confirmation is not  VLID')
            raise ValidationError('Confirm & Password is not equal!')
        return self.cleaned_data['confirm']
    class Meta:
        model  = User
        fields = ('username', 'password', 'confirm','email')
        widgets = {
            'password':forms.PasswordInput,
            'username':forms.TextInput(attrs={'class':'registration font-weight-bold','placeholder':'Your name'}),
            'email':forms.TextInput(attrs={'class':'registration font-weight-bold', 'placeholder':'Email','type':'email'}),
            'password':forms.TextInput(attrs={'class':'registration font-weight-bold','placeholder':'Password'}),
            'confirm':forms.TextInput(attrs={'class':'registration font-weight-bold','placeholder':'Confirm Password'})

        }
        help_texts = {
            'email': '',
            'username': ''
        }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)