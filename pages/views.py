from django.http import HttpResponse, JsonResponse
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
            issues = Issue.objects.all()
            ctx = {
                'reported_by_you': reported_by_you,
                'projects': projects,
                'form': form,
                'issues': issues
            }
            return render(request, 'HomePage.html', ctx)
        else:
            return redirect(f'/profil/{request.user.id}')

    def post(self, request):

        issue_name = request.POST.get('issue_name')
        issue_type = request.POST.get('issue_type')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        att = request.FILES.get('att')
        user_id = request.user.id
        employee_id = Employee.objects.get(account_id=user_id)


        try:
            new_bug = Issue()
            new_bug.issue_name = issue_name
            new_bug.issue_type = issue_type
            new_bug.project = Project.objects.get(id=5)
            new_bug.reported = employee_id
            new_bug.priority = priority
            new_bug.due_date = due_date
            new_bug.description = description
            new_bug.status = 'New'
            new_bug.attachment = att
            new_bug.save()
            ctx = {
                'error': False,
                'errorMessage': 'Successfully added'
            }
            return JsonResponse(ctx, safe=False)
        except:
            ctx = {
                'error': True,
                'errorMessage': 'Fail'
            }
            return JsonResponse(ctx, safe=False)


class ProjectDetalisView(LoginRequiredMixin, View):

    def get(self, requet, id):
        form = BugReportForm()
        project = Project.objects.get(pk=id)
        issues = Issue.objects.filter(project=project)
        ctx = {
            'project': project,
            'issues': issues,
            'form': form
        }
        return render(requet, 'projectDetalisPage.html', ctx)


class NewBugView(LoginRequiredMixin, View):


    def get(self, request):
        form = BugReportForm()
        ctx = {
            'form': form,
        }
        return render(request, 'bugReportFormPage.html', ctx)



class ProfilFormView(LoginRequiredMixin, View):


    def get(self, request, id):
        user_id = request.user.id
        employee = Employee.objects.filter(account_id=user_id)
        if employee:
            person = Employee.objects.get(account_id=user_id)
            ctx = {
                'employee': person
            }
            return render(request, 'profilPage.html', ctx)
        else:
            form = ProfilForm()
            ctx = {
                'user_id':user_id,
                'form': form,
            }
            return render(request, 'profilFormPage.html', ctx)


    def post(self, request, id):
        # form = ProfilForm(request.POST, request.FILES)

        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        position = request.POST.get('position')
        profil_pic = request.FILES.get('profilPic')

        try:

            new_employee = Employee()
            new_employee.account = request.user
            new_employee.first_name = first_name
            new_employee.last_name = last_name
            new_employee.position = position
            new_employee.email = request.user.email
            new_employee.profil_pic = profil_pic
            new_employee.save()
            return redirect('/homePage')
        except:
            ctx = {
                'error': True,
                'errorMessage': 'Fail'
            }
            return JsonResponse(ctx, safe=False)



class ProfileView(LoginRequiredMixin, View):

    def get(self, request, id):
        logged_user_id = request.user.id
        employee = Employee.objects.filter(pk=id)

        if len(employee) == 1:
            reported_by_this_dev = Issue.objects.filter(reported_id=id)
            person = Employee.objects.get(pk=id)
            projects = Project.objects.filter(devs=id)
            ctx = {
                    'employee': person,
                    'reported_by_this_dev': reported_by_this_dev
                }
            return render(request, 'profilPage.html', ctx)
        else:
            return redirect(f'/profil/{logged_user_id}')



def delete_issue(request, id):
    issue = Issue.objects.get(pk=id)
    issue.delete()
    return redirect('/homePage')

def update_status(request):
    id = request.POST.get('id')
    value = request.POST.get('value')
    issue = Issue.objects.get(pk=id)
    issue.status = value
    issue.save()
    return JsonResponse({'success': 'Status Updated'})