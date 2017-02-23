from django import forms
from user_management.models import User
from library_management.models import Song

class NewSongForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter song name'}))
    song_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Choose file'}))


    def save(self):
        user = User.objects.get(id=self.cleaned_data['user_id'])
        # import ipdb; ipdb.set_trace()
        song_instance = Song.objects.create(user_id=user,
                                            name=self.cleaned_data['name'],
                                            song_file=self.cleaned_data['song_file'])
        return song_instance
