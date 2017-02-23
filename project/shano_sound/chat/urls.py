from django.conf.urls import url
from chat.views import ChatFormView


urlpatterns = [
    url(r'chat_window/(?P<user_id>\d+)/(?P<chatroom_id>\d+)',
        ChatFormView.as_view(), name='chat'),
]
