from datetime import datetime, timezone
from random import randint
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse, redirect

from accounts.forms import MyUserCreationForm
from .models import CustomUser, EmailVerification
from django.core.mail import send_mail
from sajilo_nepal.settings import EMAIL_HOST_USER


def login(request):
    if request.user.is_authenticated:
        if request.user:
            return redirect('/')
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user:
                return redirect('/')
            else:
                return redirect('/')
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            context = {"errors": "Email or password is incorrect", "email": request.POST['email']}
            return render(request, 'accounts/logi'
                                   'n.html', context)

        if request.user:
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'accounts/login.html')


def register(request,user_type):
    if request.user.is_authenticated:
        if request.user:
            return redirect('dashboard:home')
    context = {'form': MyUserCreationForm()}
    context["vendor"]=user_type.upper()
    if request.method == 'POST':
        data=request.POST.copy()

        if user_type=='vendor':
            data["is_vendor"]=True
        else:
            data["is_vendor"]=False

        email = request.POST.get('email')
        context['email'] = email
        if request.user.is_authenticated:
            return redirect('/')
        form = MyUserCreationForm(data)
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'] = 'Password and conform Password didnot match'
            context['email'] = request.POST['email']
            context['username'] = username
            return render(request, 'accounts/register.html', context)
        if form.is_valid():
            form.save()
            email = email
            password = password1
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('accounts:send_email_verification_code')
            else:
                context['errors'] = "something went wrong"
                return render(request, 'accounts/login.html', context)
        else:
            context['errors'] = form.errors
            context['email'] = request.POST['email']
            context['username'] = username

    return render(request, 'accounts/register.html', context)

# sending email verification code
@login_required()
def send_email_verification_code(request):
    user = request.user
    if CustomUser.objects.get(email=request.user).is_email_verified:
        return HttpResponse('email already Verified')
    code = randint(100000, 999999)  # verification code
    create_date = datetime.now()
    total_try_requests = 0

    if not EmailVerification.objects.filter(users=user).exists():
        EmailVerification.objects.create(
            users=user,
            verification_code=code,
            created_date_time=create_date,
            total_try_request=total_try_requests,
        )
    else:
        email_verification = EmailVerification.objects.get(users=user)
        block_date = email_verification.block_time
        now = datetime.now(timezone.utc)
        difference = now - block_date
        if difference.total_seconds() < 300:
            return HttpResponse(f'You have been block for {difference} second')
        EmailVerification.objects.filter(users=user).update(
            verification_code=code,
            created_date_time=create_date,
            total_try_request=total_try_requests,
        )
    send_mail(
        "Email Verification Code",
        f"Your email verification code is {code}",
        EMAIL_HOST_USER,
        [EmailVerification.objects.get(users=user).users.email],
    )
    return redirect('accounts:verify_email')

@login_required()
def verify_email(request):
    if CustomUser.objects.get(email=request.user).is_email_verified:
        return redirect('my_profile:profile_create')
    if request.method == 'POST':
        if CustomUser.objects.get(email=request.user).is_email_verified:
            return redirect('my_profile:profile_create')

        request_code = request.POST['otp1'] + request.POST['otp2'] + request.POST['otp3'] + request.POST['otp4'] + \
                       request.POST['otp5'] + request.POST['otp6']  # code send from user to verify
        code = EmailVerification.objects.get(users=request.user).verification_code
        if request_code == code:
            user =CustomUser.objects.get(email=request.user)
            user.is_email_verified=True
            user.save()
            is_vendor=user.is_vendor
            if is_vendor:
                return redirect('profiles:venodr_create')
            return redirect('profiles:customer_create')
        else:
            context = {'error': 'code you have entered is wrong'}
            return render(request, 'accounts/verify_email.html', context)
    return render(request, 'accounts/verify_email.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
