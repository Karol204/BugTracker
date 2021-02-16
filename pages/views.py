from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Project, Employee, Issue
from .forms import BugReportForm, ProfilForm

# Create your views here.

class LandingPage(View):

    def get(self, request):
        return render(request, 'home.html')


class HomePage(View):

    def get(self, request):
        user_id = request.user.id
        employee = Employee.objects.filter(account_id=user_id)
        if len(employee) == 1:
            employee_id = Employee.objects.get(account_id=user_id).id
            projects = Project.objects.filter(devs__id=employee_id)
            issues = Issue.objects.all()
            print(issues)
            ctx = {
                'projects': projects,
                'issues': issues
            }
            return render(request, 'HomePage.html', ctx)
        else:
            return redirect('/profil')


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

    def get(self, request, id):
        user_id = request.user.id
        employee = Employee.objects.filter(account_id=user_id)
        print(employee)

        if employee:
            person = Employee.objects.get(account_id=user_id)
            ctx = {
                'employee': person,
            }
            return render(request, 'profilPage.html', ctx)
        else:
            return redirect('/profil')


class ProfilFormView(View):

    def get(self, request):
        form = ProfilForm()
        ctx = {
            'form': form,
        }
        return render(request, 'profilFormPage.html', ctx)

    def post(self, request):
        form = ProfilForm(request.POST)
        if form.is_valid():
            new_employee = Employee()
            new_employee.account = request.user
            new_employee.first_name = form.cleaned_data['first_name']
            new_employee.last_name = form.cleaned_data['last_name']
            new_employee.position = form.cleaned_data['position']
            new_employee.email = form.cleaned_data['email']
            new_employee.save()
        return redirect('/homePage')