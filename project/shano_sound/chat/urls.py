from django.conf.urls import url
from chat.views import CreateChatView


urlpatterns = [
    url(r'chat', CreateChatView.as_view())
]
