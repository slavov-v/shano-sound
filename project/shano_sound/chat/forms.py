from django import forms
from chat.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content', 'membership', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membership'].required = False
        self.fields['membership'].widget = forms.HiddenInput()
