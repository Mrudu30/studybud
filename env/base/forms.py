from django.forms import ModelForm
from .models import Room,Message

# create class for the form
class roomform(ModelForm):
    class Meta:
        model = Room
        fields = ('topic','name','desc')
        
# for message editing
class messageEdit(ModelForm):
    class Meta:
        model = Message
        fields = ('body',) 