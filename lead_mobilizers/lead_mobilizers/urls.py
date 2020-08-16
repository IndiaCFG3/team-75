"""lead_mobilizers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from lead_mobilizers import views as lead_mobilizers_views
from mobilizers import views as mobilizers_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lead_mobilizers_views.home,name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='mobilizers/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mobilizers/logout.html'), name='logout'),
    
    path('mobilizers/activities/',mobilizers_views.activities,name='mobilizers-activites'), 
    path('mobilizers/create/',mobilizers_views.create,name='mobilizers-create'),
    path('mobilizers/leads/',mobilizers_views.leads,name='mobilizers-leads'),

]
