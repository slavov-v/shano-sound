from django import forms
from user_management.models import User
from library_management.models import Song

class NewSongForm(forms.Form):
    name = forms.CharField(max_length=50)
    song_file = forms.FileField()


    def save(self):
        user = User.objects.get(id=self.cleaned_data['user_id'])
        # import ipdb; ipdb.set_trace()
        Song.objects.create(user_id=user, name=self.cleaned_data['name'],
                            song_file=self.cleaned_data['song_file'])
