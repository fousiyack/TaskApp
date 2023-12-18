# accounts/utils.py

import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models  import OTPModel


def generate_and_save_otp(user):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    otp_model, created = OTPModel.objects.get_or_create(user=user, defaults={'otp_code': otp})
    return otp

def validate_otp(user_email, otp_entered):
    try:
        stored_otp = OTPModel.objects.get(email=user_email).otp
        return stored_otp == otp_entered
    except OTPModel.DoesNotExist:
        return False

def send_otp_email(email, otp):
    subject = 'Your OTP for Login'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)