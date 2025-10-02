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

class FilterForm(forms.Form):

    PRIORITY_CHOICES = [
        ("", "Усі пріорітети"),
        ("Low", "Низький пріорітет"),
        ("Medium", "Середній пріорітет"),
        ("High", "Високий пріорітет"),

    ]
    STATUS_CHOICES = [
        ("", "Усі статуси"),
        ("Pending", "Потрібно виконати"),
        ("In-progress", "В процесі"),
        ("Done", "Виконано"),

    ]

   
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, label='Пріоритет', required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус', required=False)

      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })

      