
from django.urls import path
from .views import *

urlpatterns = [
    path('',registerView.as_view(),name='register' ),
    path('userLogin/',userLogin.as_view(),name='userLogin' ),
    path('otp/',OtpView.as_view(),name='otp'),
    path('logout/',logout,name='user-logout'),

]
