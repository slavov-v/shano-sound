from chat.models import Message
from user_management.models import BaseUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import json

@login_required
def chat(request):
    messages = Message.objects.all()
    online_users = BaseUser.objects.filter(is_online=True)
    return render(request, "chat.html", locals())

@login_required
def send_message(request):
    user = request.user
    message = Message.objects.create(sender=user,
                                     content=request.POST.get("message"))
    message.save()
    return HttpResponse(json.dumps({"user": user.email, "message": message.content}), content_type="text/json")

@login_required
def get_messages(request):
    messages = Message.objects.all()
    res = []
    for m in messages:
        res.append({"user": m.sender.email, "message": m.content})
    return HttpResponse(json.dumps(res), content_type="text/json")
