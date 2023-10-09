from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout', logout_view, name = 'logout'),
    path('signup/', signup_view, name = 'signup'),

    path('password_reset/', password_reset_view, name = 'password-reset'),
    # path('/password_reset_confirm/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
]