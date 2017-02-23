from django.conf.urls import url
from library_management.views import MyMusicView, NewSongView, PlaySongView, FriendPlaylistView

urlpatterns = [
    url(r'mymusic/(?P<pk>[0-9]+/$)', PlaySongView.as_view(), name='play'),
    url(r'mymusic/$', MyMusicView.as_view(), name='my_music'),
    url(r'newsong/$', NewSongView.as_view(), name='new_song'),
    url(r'playlist/(?P<pk>[0-9]+/$)', FriendPlaylistView.as_view(), name='friend-music'),
]
