from django import forms
from .models import Project, Employee, Issue

Types = (
    ('Bug', 'Bug'),
    ('Data', 'Database'),
    ('Front', 'Front-end')
)

Priority = (
    ('Urgent', 'Urgent'),
    ('ASAP', 'ASAP'),
    ('Normal', 'Normal')
)

Status = (
    ('New', 'New'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done')
)

class BugReportForm(forms.Form):

    issue_name = forms.CharField(max_length=250)
    issue_type = forms.ChoiceField(choices=Types)
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    priority = forms.ChoiceField(choices=Priority)
    due_date = forms.DateField()
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    description = forms.CharField(max_length=250)
    attachment = forms.FileField()

class ProfilForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'email', 'profil_pic']