from django.contrib import admin
from django.urls import path, include
from .views import LandingPage, HomePage, ProjectDetalisView, delete_issue, NewBugView, ProfileView, ProfilFormView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landingPage'),
    path('homePage', HomePage.as_view(), name='home'),
    path('projectDetails/<int:id>', ProjectDetalisView.as_view(), name='projectDetails'),
    path('reportNewBug', NewBugView.as_view(), name='reportNewBug'),
    path('profileView/<int:id>', ProfileView.as_view(), name='profile'),
    path('profil', ProfilFormView.as_view(), name='profileForm'),
    path('delete/<int:id>', delete_issue)
]
