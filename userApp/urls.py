
from django.urls import path
from .views import *

urlpatterns = [
    path('',registerView.as_view(),name='register' ),
    # path('userLogin/',userLogin,name='userLogin' ),
    path('otp/',OtpView.as_view(),name='otp' ),

]
