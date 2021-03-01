from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Project, Employee, Issue
from .forms import BugReportForm, ProfilForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class LandingPage(View):

    def get(self, request):
        return render(request, 'home.html')



class HomePage(LoginRequiredMixin, View):

    def get(self, request):
        form = BugReportForm()
        user_id = request.user.id

        employee = Employee.objects.filter(account_id=user_id)
        if len(employee) == 1:
            employee_id = Employee.objects.get(account_id=user_id).id
            reported_by_you = Issue.objects.filter(reported_id=employee_id)
            projects = Project.objects.filter(devs=employee_id)
            ctx = {
                'reported_by_you': reported_by_you,
                'projects': projects,
                'form': form
            }
            return render(request, 'HomePage.html', ctx)
        else:
            return redirect('/profil')

    def post(self, request):

        issue_name = request.POST.get('issue_name')
        issue_type = request.POST.get('issue_type')
        project = request.POST.get('project')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        user_id = request.user.id
        employee_id = Employee.objects.get(account_id=user_id)
        new_bug = Issue()
        new_bug.issue_name = issue_name
        new_bug.issue_type = issue_type
        new_bug.project = Project.objects.get(id=project)
        new_bug.reported = employee_id
        new_bug.priority = priority
        new_bug.due_date = due_date
        new_bug.description = description
        new_bug.save()
        return HttpResponse('Success')


class ProjectDetalisView(LoginRequiredMixin, View):

    def get(self, requet, id):
        project = Project.objects.get(pk=id)
        ctx = {
            'project': project
        }
        return render(requet, 'projectDetalisPage.html', ctx)


class NewBugView(LoginRequiredMixin, View):


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
            priority = form.cleaned_data['priority']
            due_date = form.cleaned_data['due_date']
            description = form.cleaned_data['description']
            user_id = request.user.id
            employee_id = Employee.objects.get(account_id=user_id)
            new_bug = Issue()
            new_bug.issue_name = issue_name
            new_bug.issue_type = issue_type
            new_bug.project = project
            new_bug.reported = employee_id
            new_bug.priority = priority
            new_bug.due_date = due_date
            new_bug.description = description
            new_bug.save()
        return redirect('home')


class ProfileView(LoginRequiredMixin, View):

    def get(self, request, id):
        user_id = request.user.id
        employee = Employee.objects.filter(account_id=user_id)

        if employee:
            person = Employee.objects.get(account_id=user_id)
            ctx = {
                'employee': person,
            }
            return render(request, 'profilPage.html', ctx)
        else:
            return redirect('/profil')


class ProfilFormView(LoginRequiredMixin, View):


    def get(self, request):
        user_id = request.user.id
        employee = Employee.objects.filter(account_id=user_id)
        if employee:
            person = Employee.objects.get(account_id=user_id)
            form = ProfilForm(isinstance(person))
        else:
            form = ProfilForm()
        ctx = {
            'form': form,
        }
        return render(request, 'profilFormPage.html', ctx)


    def post(self, request):
        form = ProfilForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
        return redirect('/homePage')


def delete_issue(request, id):
    issue = Issue.objects.get(pk=id)
    issue.delete()
    return redirect('/homePage')