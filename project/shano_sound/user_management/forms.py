from django import forms
from user_management.models import BaseUser
from hashlib import sha256


class RegisterAndLoginForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = ['email', 'password', 'first_name', 'last_name']
        labels = {'email': 'E-mail',
                  'password': 'Password'}
        widgets = {'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter password'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter e-mail'})}

    def save(self, commit=True):
        user = BaseUser.objects.create_user(email=self.cleaned_data.get('email'),
                                            password=self.cleaned_data.get('password'),
                                            first_name=self.cleaned_data.get('first_name'),
                                            last_name=self.cleaned_data.get('last_name'))
        user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter password'}))


class AddFriendForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder': 'Enter friend\'s e-mail'}))

    def save(self, **kwargs):
        # import ipdb; ipdb.set_trace()
        current_user = BaseUser.objects.get(email=kwargs.get('email'))
        search_user = BaseUser.objects.get(email=self.cleaned_data.get('email'))
        current_user.friends.add(search_user)
        search_user.friends.add(current_user)
        current_user.save()
        search_user.save()
