from django.conf.urls import url
from chat.views import chat, send_message, get_messages

urlpatterns = [
    url(r'send-message$', send_message, name="send_message"),
    url(r'get-messages$', get_messages, name="get_message"),
    url(r'chat/$', chat, name='chat'),
]
