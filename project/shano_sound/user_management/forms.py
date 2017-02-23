from django import forms
from user_management.models import User
from hashlib import sha256


class RegisterAndLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {'email': 'E-mail',
                  'password': 'Password'}
        widgets = {'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter password'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter e-mail'})}

    def clean_password(self):
        return self.hash_password()

    def hash_password(self):
        password = self.cleaned_data.get('password')
        password = sha256(password.encode('utf-8')).hexdigest()
        return password

class AddFriendForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder': 'Enter friend\'s e-mail'}))

    def save(self, **kwargs):
        # import ipdb; ipdb.set_trace()
        current_user = User.objects.get(email=kwargs.get('email'))
        search_user = User.objects.get(email=self.cleaned_data.get('email'))
        current_user.friends.add(search_user)
        search_user.friends.add(current_user)
        current_user.save()
        search_user.save()
