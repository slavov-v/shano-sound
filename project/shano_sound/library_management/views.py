import os
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, View
from django.core.files import File
from library_management.models import Song
from user_management.models import User
from library_management.forms import NewSongForm
# Create your views here.


class MyMusicView(ListView):
    model = Song
    template_name = 'song_list.html'

    def get_queryset(self):
        user = User.objects.get(email=self.request.session['email'])
        return Song.objects.filter(user_id=user)


class NewSongView(View):
    def get(self, request):
        form = NewSongForm()
        return render(request, 'new_song_form.html', locals())

    def post(self, request):
        form = NewSongForm(request.POST, request.FILES)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            # import ipdb; ipdb.set_trace()
            user_id = User.objects.get(email=request.session['email']).id
            form.cleaned_data['user_id'] = user_id
            form.save()
        print(form.errors)
        return redirect('/mymusic')

class PlaySongView(View):
    def get(self, request, **kwargs):
        song_id = int(self.kwargs['pk'][:-1])
        song = Song.objects.get(id=song_id)
        user = User.objects.get(email=self.request.session['email'])
        object_list = Song.objects.filter(user_id=user)

        file_name = str(song.song_file)
        f = File(open(file_name, 'rb'))
        response = render(request, 'song_list.html', locals())
        response.write(f.read())

        response['Content-Type'] = 'audio/mp3'
        response['Content-Length'] = os.path.getsize(file_name)
        return response
