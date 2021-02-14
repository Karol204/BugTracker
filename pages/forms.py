from django import forms
from .models import Project

Types = (('Bug', 'Bug'), ('Data', 'Database'), ('Front', 'Front-end'))

class BugReportForm(forms.Form):

    issue_name = forms.CharField(max_length=250)
    issue_type = forms.CharField()
    project = forms.ModelChoiceField(queryset=Project.objects.all())
