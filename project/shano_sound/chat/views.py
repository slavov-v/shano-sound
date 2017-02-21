from django.views.generic import CreateView
from chat.models import Chat, Message


class CreateChatView(CreateView):
    template_name = 'chat_form.html'
    model = Chat
    fields = '__all__'


class CreateMessageView(CreateView):
    template_name = 'chat_form.html'
    model = Message
    fields = '__all__'
