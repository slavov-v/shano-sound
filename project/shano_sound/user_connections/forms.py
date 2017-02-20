from django import forms
from user_connections.models import Connection


class ConnectionForm(forms.Form):
    class Meta:
        model = Connection
        fields = '__all__'
        labels = {'user_id_1': 'Your username',
                  'user_id_2': 'Friend username'}
