from django.shortcuts import render
from django.views import View
from .models import Project, Employee, Issue

# Create your views here.

class LandingPage(View):

    def get(self, request):
        return render(request, 'home.html')


class HomePage(View):

    def get(self, request):
        user_id = request.user.id
        employee_id = Employee.objects.get(account_id=user_id).id
        projects = Project.objects.filter(devs__id=employee_id)
        ctx = {
            'projects': projects
        }
        return render(request, 'firstPage.html', ctx)