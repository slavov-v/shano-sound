from django.views.generic import FormView, CreateView
from chat.models import Message, MembershipInChat
from chat.forms import MessageForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class ChatFormView(CreateView):
    template_name = 'chat_window.html'
    model = Message
    form_class = MessageForm

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        membership = MembershipInChat.objects.get(chat_room__id=self.kwargs['chatroom_id'],
                                                     user__id=self.kwargs['user_id'])
        initial['membership'] = membership
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        current_chatroom_id = self.kwargs['chatroom_id']
        memberships = MembershipInChat.objects.filter(chat_room=current_chatroom_id)
        messages = []
        for membership in memberships:
            for message in Message.objects.filter(membership=membership.id):
                messages.append(message.content)
        context['messages'] = messages

        return context

    def get_success_url(self, **kwargs):
        if self.kwargs is not None:
            return reverse('chat', kwargs=self.kwargs)
