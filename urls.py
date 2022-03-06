from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('facultysignup',views.facultysignup,name='facultysignup'),
    path('login',views.login,name='login'),
    path('facultylogin',views.faculty_login,name='facultylogin'),
    path('thankyou',views.thankyou,name='thankyou'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

