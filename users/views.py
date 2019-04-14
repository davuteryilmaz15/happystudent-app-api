from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from happyapi.utils import send_mail_via_gmail_smtp
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
# generics.CreateAPIView -> only POST
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class UserActivate(APIView):
    permission_classes = ()

    def get(self, request, token):
        try:
            t = Token.objects.get(key=token)
            user = User.objects.get(id=t.user_id)
            user.is_active = 1
            user.save()
        except:
            return Response({'error':'invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message':'User successfuly activated.'})

class UserForgetPassword(APIView):
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        new_password = request.data.get('new_password')
        user = User.objects.get(email=email)
        if user:
            # if Token does not exists then create it.
            # if Token does exists then refresh it.
            token, created =  Token.objects.get_or_create(user=user)
            if token:
                new_token = token.key + new_password
                message = '<a href="http://127.0.0.1:8000/api/users/forget_password/'+new_token+'/">Confirm Password</a>'
                
                send_mail_via_gmail_smtp(email, message)

            data = {
                "token" : new_token or None
            }
            return Response(data)
        else:
            data = {
                "error" : "Invalid email."
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserForgetPasswordConfirm(APIView):
    permission_classes = ()
    def get(self, request, token):
        try:
            # token = token + new_password
            if len(token) < 41:
                return Response({'error':'invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                new_password = token[40:]
                token = token[:40]

            t = Token.objects.get(key=token)
            user = User.objects.get(id=t.user_id)
            if user:
                user.set_password(new_password)
                user.save()
            else:
                return Response({'error':'invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message':'Password has been changed.'})


class UserLogin(APIView):
    permission_classes = ()

    def post(self, request):
        """ 
        Add this Parameter to post body.
        ---
        {
            "username":"",
            "password":""
        }
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # if Token does not exists then create it.
            # if Token does exists then refresh it.
            token, created =  Token.objects.get_or_create(user=user)
            if token:
                token.delete()
                token = Token.objects.create(user=user)
            data = {
                "token" : user.auth_token.key
            }
            return Response(data)
        else:
            data = {
                "error" : "Wrong Credentials."
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


