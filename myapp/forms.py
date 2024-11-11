from django import forms
from .models import *

class userform(forms.ModelForm):
    class Meta:
        model=user10
        # fields='__all__'
        fields=['user_name']
        def clean_username(self):
            username=self.cleaned_data.get('username')
            if len(username)<3:
                raise forms 
            
class profile(forms.ModelForm):
    class Meta:
        model=userProfile
        fields='__all__'

class postform(forms.ModelForm):
    class Meta:
        model=Post1
        fields='__all__'

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields='__all__'
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError("password does not match")
        return password



