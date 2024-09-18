from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'service', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }
        
         
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       placeholders = {
                        'name': 'Name*',
                        'email': 'Email*',
                        'service': 'Service',
                        'phone':'Phone',
                        'message': 'How can we help you?'
                    }
  
       for field_name, field in self.fields.items():
           field.widget.attrs['class'] = 'form-control'
           field.label = ''
           if field_name in placeholders:
               field.widget.attrs['placeholder'] = placeholders[field_name]
               

# Register & Login Forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control', 'name': 'username'}))
    password = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control', 'name': 'password'}))

    # class Meta:
    #     model = User
    #     fields = ['username', 'password']
    
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="İstifadəçi adı")
    password = forms.CharField(max_length=10, label="Şifrə", widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=10, label="Şifrəni təsdiqlə", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 3:
            raise forms.ValidationError("Username is too short")
        return username 

    def clean_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password   
    

        


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['com_name','com_email','com_message','com_rate']
    



class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['per_name', 'per_email', 'per_number', 'per_service_type', 'per_country',
                  'per_house_number', 'per_apartment', 'per_town', 'per_city', 'per_zip',
                  'per_notes', 'per_payment_method']
