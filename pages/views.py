from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Project, Employee, Issue
from .forms import BugReportForm

# Create your views here.

class LandingPage(View):

    def get(self, request):
        return render(request, 'home.html')


class HomePage(View):

    def get(self, request):
        user_id = request.user.id
        employee_id = Employee.objects.get(account_id=user_id).id
        projects = Project.objects.filter(devs__id=employee_id)
        print(projects)
        ctx = {
            'projects': projects
        }
        return render(request, 'HomePage.html', ctx)


class ProjectDetalisView(View):

    def get(self, requet, id):
        project = Project.objects.get(pk=id)
        ctx = {
            'project': project
        }
        return render(requet, 'projectDetalisPage.html', ctx)


class NewBugView(View):

    def get(self, request):
        form = BugReportForm()
        ctx = {
            'form': form,
        }
        return render(request, 'bugReportFormPage.html', ctx)

    def post(self, request):
        form = BugReportForm(request.POST)
        if form.is_valid():
            issue_name = form.cleaned_data['issue_name']
            issue_type = form.cleaned_data['issue_type']
            project = form.cleaned_data['project']
            user_id = request.user.id
            employee_id = Employee.objects.get(account_id=user_id)
            new_bug = Issue()
            new_bug.issue_name = issue_name
            new_bug.issue_type = issue_type
            new_bug.project = project
            new_bug.reported = employee_id
            new_bug.save()
        return redirect('home')


class ProfileView(View):

    def get(self, request):
        user_id = request.user.id
        employee = get_object_or_404(Employee, account_id=user_id)
        print(employee)
        if employee:
            profile = True
        else:
            profile = False
        print(profile)
        ctx = {
            'profile': profile
        }
        return render(request, 'profilPage.html', ctx)