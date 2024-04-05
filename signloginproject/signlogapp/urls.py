from django.urls import path

from signlogapp import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('reg',views.signup_fun,name='reg'),
]