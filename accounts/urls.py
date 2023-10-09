from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views

# from django.contrib.auth.views import ( 
#     PasswordResetView, 
#     PasswordResetDoneView, 
#     PasswordResetConfirmView,
#     PasswordResetCompleteView
# )

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout', logout_view, name = 'logout'),
    path('signup/', signup_view, name = 'signup'),


    path('password_reset/', password_reset_view, name = 'password-reset'),
    path('/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('/password_reset_confirm/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
]