import os
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, View
from django.core.files import File
from django.utils.decorators import method_decorator
from library_management.models import Song
from user_management.models import User
from library_management.forms import NewSongForm
from user_management.decorators import login_required
from library_management.helpers import SongMetadataLoader
from django.contrib.auth.mixins import LoginRequiredMixin
from user_management.models import BaseUser
# Create your views here.

# @method_decorator(login_required, name="dispatch")
class MyMusicView(LoginRequiredMixin, ListView):
    model = Song
    template_name = 'song_list.html'

    def get_queryset(self):
        user = BaseUser.objects.get(email=self.request.user.email)
        return Song.objects.filter(user_id=user)

# @method_decorator(login_required, name="dispatch")
class FriendPlaylistView(LoginRequiredMixin, ListView):
    model = Song
    template_name = 'friend_song_list.html'

    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        user = BaseUser.objects.get(id=int(self.kwargs['pk'][:-1]))
        return Song.objects.filter(user_id=user)

# @method_decorator(login_required, name="dispatch")
class NewSongView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewSongForm()
        return render(request, 'new_song_form.html', locals())

    def post(self, request):
        form = NewSongForm(request.POST, request.FILES)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            import ipdb; ipdb.set_trace()
            user_id = BaseUser.objects.get(email=request.user.email).id
            form.cleaned_data['user_id'] = user_id
            song_instance = form.save()
        print(form.errors)
        loader = SongMetadataLoader(song_instance)
        loader.populate_metada_for_song()
        return redirect('/mymusic')


class PlaySongView(View):
    def get(self, request, **kwargs):
        song_id = int(self.kwargs['pk'][:-1])
        song = Song.objects.get(id=song_id)
        user = BaseUser.objects.get(email=self.request.user.email)
        object_list = Song.objects.filter(user_id=user)

        file_name = str(song.song_file)
        f = File(open(file_name, 'rb'))
        response = render(request, 'song_list.html', locals())
        response.write(f.read())

        response['Content-Type'] = 'audio/mp3'
        response['Content-Length'] = os.path.getsize(file_name)
        return response
