from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'priority','status', 'file']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })

        self.fields['deadline'].widget = forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control mb-2'})