from django import forms
from user_management.models import User
from hashlib import sha256


class RegisterAndLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'E-mail',
                  'password': 'Password'}
        widgets = {'password': forms.PasswordInput()}

    def clean_password(self):
        return self.hash_password()

    def hash_password(self):
        password = self.cleaned_data.get('password')
        password = sha256(password.encode('utf-8')).hexdigest()
        return password
