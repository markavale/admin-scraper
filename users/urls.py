from django.urls import path,include
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView, LoginView
from . views import  UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='User')

urlpatterns = [ 
    path('', include(router.urls)),
    path('', include('dj_rest_auth.urls')),
    path('login-user/', LoginView.as_view(), name='login'),
    # path('user-details/', UserProfileView.as_view(), name='user-profile'),
    path('registration/', include('dj_rest_auth.registration.urls'), name='register'),
    path('registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
