from django.forms import ModelForm
from .models import Notes

class NoteForm(ModelForm):
    
    class Meta:
        model = Notes
        fields = '__all__'
