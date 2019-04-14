from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.authtoken.models import Token
from happyapi.utils import send_mail_via_gmail_smtp

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

        extra_kwargs = {'user':{'read_only':True}}

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'password':{'read_only':True},
            'password':{'write_only':True},# We also don’t want to get back the password in response
            'email':{'required':True},
            'first_name':{'required':True},
            'last_name':{'required':True},
        }
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active = 0,
        )
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, **validated_data['profile'])
        Token.objects.create(user=user) #Activate islemi icin

        #send mail
        message = '<a href="http://127.0.0.1:8000/api/users/activate/'+user.auth_token.key+'/">activate account</a>'
        to_addr = user.email

        send_mail_via_gmail_smtp(to_addr,message)

        return user
        
