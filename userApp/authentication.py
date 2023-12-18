# myapp/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from .utils import validate_otp

class OTPAuthentication(BaseAuthentication):
    def authenticate(self, request):
        otp = request.headers.get('Authorization')

        if not otp:
            return None

        # Assuming you have the user's email in the request or wherever you store it
        user_email = request.data.get('email')

        if not user_email:
            raise AuthenticationFailed('Email not provided')

        if not validate_otp(user_email, otp):
            raise AuthenticationFailed('Invalid OTP')

        User = get_user_model()
        try:
            user = User.objects.get(email=user_email)
            return user, None
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
