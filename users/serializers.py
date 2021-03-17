from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from dj_rest_auth.serializers import PasswordResetSerializer, LoginSerializer, PasswordResetSerializer
from rest_framework.authtoken.models import Token
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'max_length': 68}
            }

class RegisterUserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'max_length': 68}
            }

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        # elif 
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self) :
        return {
            'email_template_name': 'email/user_reset_password.html'
        }

        
    # def save(self):
    #     request = self.context.get('request')
    #     # Set some values to trigger the send_email method.
    #     opts = {
    #         'use_https': request.is_secure(),
    #         'from_email': settings.EMAIL_HOST_USER, 
    #         'request': request,
    #         # here I have set my desired template to be used
    #         # don't forget to add your templates directory in settings to be found
    #         'email_template_name': 'email/user_reset_password.html'
    #     }

    #     opts.update(self.get_email_options())
    #     self.reset_form.save(**opts)

class CustomLoginSerializer(LoginSerializer):

    def validate(self, attrs):
        username = attrs.get('username', '')
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and not user.active:
            print(True)
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        return super().validate(attrs)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

# class VerifyEmailSerializer(serializers.ModelSerailizer):
