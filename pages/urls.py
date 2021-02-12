from django.contrib import admin
from django.urls import path, include
from .views import LandingPage, HomePage

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landingPage'),
    path('/', HomePage.as_view(), name='home'),

]
