from django.shortcuts import render
from django.views.generic import CreateView
from user_connections.models import Connection


class ConnectionView(CreateView):
    model = Connection
    fields = '__all__'
    template_name = 'connection_panel.html'
    success_url = "thanks"

    def save(self):
        data = self.clean_data
        Connection.objects.create(user_id_1=data['user_id_1'], user_id_2=data['user_id_2'])


def thanks(request):
    all_connections = Connection.objects.all()
    return render(request, 'thanks.html', locals())
