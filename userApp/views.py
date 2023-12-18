from django.shortcuts import render,redirect
from rest_framework import generics,status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegistrationSerializer
# ,LoginSerializer
from .utils import send_otp_email,generate_and_save_otp
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
# from passlib.hash import django_pbkdf2_sha256 as handler


from django.contrib.auth.models import update_last_login
from rest_framework.views import APIView
from django.utils.crypto import get_random_string
from .models import OTPModel




class registerView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    template_name = "user/register.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        request.session['email'] = user.email
        
        # Generate and send OTP to the user's email
        user_email = serializer.validated_data['email']
        otp = get_random_string(length=4, allowed_chars='1234567890')
        OTPModel.objects.create(user=user, otp=otp)
        send_otp_email(user_email, otp)

        return redirect('user/otp.html',)
        

# def userLogin(request):
#      return render(request,'user/login.html')
# class userLogin(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         email = request.data['email']
#         print('email', email)
#         filter_data = CustomUser.objects.filter(email=email).values('is_active')
#         print('filter_data', filter_data)
#         if filter_data.exists():
#             val = filter_data[0]['is_active']
#         else:
#             return Response("Email is not Registered", status=status.HTTP_400_BAD_REQUEST)

#         if val:
#             if serializer.is_valid():
#                 user = authenticate(
#                     username=request.data['email'], password=request.data['password'])
#                 update_last_login(None, user)
#                 if user is not None  and user.is_active:  
#                     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#                     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#                     payload = jwt_payload_handler(user)
#                     token = jwt_encode_handler(payload)
#                     return Response({'msg': 'Login successful', 'token': token,
#                                      'email': user.email, 
#                                      }, status=status.HTTP_200_OK)
#                 else:
#                     return Response({'msg': 'Account not approved or wrong Password.'}, status=status.HTTP_409_CONFLICT)
#             else:
#                 return Response({'msg': 'Invalid data'}, status=status.HTTP_401_UNAUTHORIZED)

#         else:
#             return Response({'Error': 'Not a valid user'}, status=status.HTTP_401_UNAUTHORIZED) 


class OtpView(APIView):
    def get(self,request):
      return render(request,'user/otp.html')
    

        