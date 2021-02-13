from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

Types = (('Bug', 'Bug'), ('Data', 'Database'), ('Front', 'Front-end'))

Positions = (('fron', 'Front-end developer'), ('back', 'Back-end developer'), ('data', 'Data scientist'),('project', 'Project manager'))

Priority = (('Urgent', 'Urgent'), ('ASAP', 'ASAP'), ('Normal', 'Normal'))

class Issue(models.Model):
    issue_name = models.CharField(max_length=250)
    issue_type = models.CharField(choices=Types, max_length=5)

    def __str__(self):
        return f'{self.issue_name}'


class Employee(models.Model):
    account = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    position = models.CharField(choices=Positions, max_length=7)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

class Project(models.Model):
    project_name = models.CharField(max_length=250)
    description = models.CharField(max_length=650)
    deadline = models.DateField()
    devs = models.ManyToManyField(Employee)
    issues = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.CharField(choices=Priority, max_length=6)
    added_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.project_name}'