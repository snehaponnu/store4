from django.urls import path
from .forms import LoginForm
from . import views
app_name='myapp'
from django.contrib.auth import views as auth_view

urlpatterns = [
path('new_page/', views.new_page, name='new_page'),
path('form/', views.form,name="form"),
path('confirm/', views.confirm,name="confirm"),
        path('', views.allCourdep, name='allCourdep'),
        path('<slug:c_slug>/',views.allCourdep,name='courses_by_department'),
        path('CustomerRegistrationView',views.CustomerRegistrationView.as_view(),name='customerregistration'),
        path('login',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
        # path('profile/',views.ProfileView.as_vew(),name='profile'),



]