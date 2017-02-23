from chat.models import Message
from user_management.models import User
from django.shortcuts import render
from django.http import HttpResponse
import json


def chat(request):
    messages = Message.objects.all()
    online_users = User.objects.filter(is_online=True)
    return render(request, "chat.html", locals())


def send_message(request):
    user = User.objects.first()
    # TODO: Take request.user intead of User.objects.first()
    message = Message.objects.create(sender=user,
                                     content=request.POST.get("message"))
    message.save()
    return HttpResponse(json.dumps({"user": user.email, "message": message.content}), content_type="text/json")


def get_messages(request):
    messages = Message.objects.all()
    res = []
    for m in messages:
        res.append({"user": m.sender.email, "message": m.content})
    return HttpResponse(json.dumps(res), content_type="text/json")
