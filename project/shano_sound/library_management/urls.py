from django.conf.urls import url
from library_management.views import MyMusicView, NewSongView, PlaySongView

urlpatterns = [
    url(r'mymusic/(?P<pk>[0-9]+/$)', PlaySongView.as_view(), name='play'),
    url(r'mymusic/$', MyMusicView.as_view(), name='my_music'),
    url(r'newsong/$', NewSongView.as_view(), name='new_song'),
]
