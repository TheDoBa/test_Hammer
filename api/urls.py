from django.urls import path
from .views import (
    SendCodeView,
    VerifyCodeView,
    ProfileView,
    ActivateInviteView,
    InvitedUsersView
)

urlpatterns = [
    path('send-code/', SendCodeView.as_view(), name='send_code'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify_code'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('activate-invite/', ActivateInviteView.as_view(), name='activate_invite'),
    path('invited-users/', InvitedUsersView.as_view(), name='invited_users'),
]
