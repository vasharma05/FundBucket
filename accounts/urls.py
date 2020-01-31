"""FundBucket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('personal_info/', views.PersonalInfoView.as_view(), name='personal_info'),
    path('logout/', LogoutView.as_view(), name='logout')
]