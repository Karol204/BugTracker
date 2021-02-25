from django import forms
from .models import Project, Employee

Types = (('Bug', 'Bug'), ('Data', 'Database'), ('Front', 'Front-end'))
Priority = (('Urgent', 'Urgent'), ('ASAP', 'ASAP'), ('Normal', 'Normal'))
class BugReportForm(forms.Form):

    issue_name = forms.CharField(max_length=250)
    issue_type = forms.CharField()
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    priority = forms.ChoiceField(choices=Priority)
    due_date = forms.DateField()
    description = forms.CharField(max_length=250)


class ProfilForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'email']