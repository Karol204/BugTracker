from django.contrib import admin
from .models import Issue, Employee, Project
# Register your models here.



class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_name', 'issue_type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'email', 'account')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'deadline', 'devs')



admin.site.register(Issue, IssueAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)