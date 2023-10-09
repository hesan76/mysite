from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import SignupForm, LoginForm, PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags



# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data= request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)    

                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = LoginForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required()
def logout_view(request):
    # if request.user.is_authenticated:
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,'Your ticket submitted seccessfully!')
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR,'Your ticket didnt submitted!')
    
        form = SignupForm()
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
    

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user is not None:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                reset_url = reverse('password_reset_confirm', args=[uid, token])
                reset_url = request.build_absolute_uri(reset_url)

                subject = 'Reset Password'
                html_message = render_to_string('accounts/password_reset_email.html', {'user': user,'reset_url': reset_url,})
                message = strip_tags(html_message)

                send_mail(subject, message, 'travelistasup23@gmail.com', [email])

                return render(request, 'accounts/password_reset_done.html', {'form': form})
    else:
        form = PasswordResetForm()
        return render(request, 'accounts/password_reset.html', {'form': form})



# def password_reset_confirm_view(request, uidb64, token):
#     UserModel = get_user_model()
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = UserModel._default_manager.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         if request.method == 'POST':
#             form = ConfirmSetPasswordForm(user, request.POST)
#             if form.is_valid():
#                 form.save()
#                 update_session_auth_hash(request, user)  
#                 return render(request, 'accounts/password_reset_complete.html', {'form': form})
#         else:
#             form = ConfirmSetPasswordForm(user)

#         return render(request, 'accounts/password_reset_confirm.html', {'form': form})
