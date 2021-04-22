from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
# from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import VerifyEmailView
from django.contrib.auth import  authenticate #login
from rest_framework import viewsets, status
from django.conf import settings


User = settings.AUTH_USER_MODEL

class UserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class VerifyEmailView(VerifyEmailView):

    def save(self, request, *args, **kwargs):
        user = super(VerifyEmailView, self).save(request)
        user.verified = True
        print(user.verified)
        return user


class LoginView(APIView):
    permission_classes = (AllowAny)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=username, email=email, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# class LoginUserView(LoginView): # For custom login
#     serializer_class = CustomLoginSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = CustomLoginSerializer(data=request.data)  # changed  to desired serializer
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         authenticate(request, user)
#         return super(LoginUserView, self).post(request)

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class UserDetailView(APIView):
    #authentication_classes = []
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"email": request.user.email})
