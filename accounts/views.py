from django.shortcuts import render
import random
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .models import UserOTP
from django.contrib.auth.models import User

def login_request(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        
        if user is not None:
            # 1. Generate a 6-digit OTP
            otp_code = str(random.randint(100000, 999999))
            
            # 2. Save/Update OTP in DB
            otp_obj, created = UserOTP.objects.get_or_create(user=user)
            otp_obj.otp = otp_code
            otp_obj.save()
            
            # 3. Send the Email
            send_mail(
                'Your Login OTP',
                f'Your OTP is {otp_code}. It expires in 5 minutes.',
                '24amtics571@gmail.com',
                [user.email],
                fail_silently=False,
            )
            
            # 4. Store user ID in session temporarily
            request.session['otp_user_id'] = user.id
            return redirect('verify_otp')
    return render(request, 'accounts/login.html')
    

def verify_otp(request):
    if request.method == "POST":
        user_id = request.session.get('otp_user_id')
        user_otp_input = request.POST.get('otp')
        
        if not user_id:
            return redirect('login_request')
            
        user = User.objects.get(id=user_id)
        otp_record = UserOTP.objects.get(user=user)
        
        if otp_record.otp == user_otp_input and otp_record.is_valid():
            login(request, user) # Official Django login
            del request.session['otp_user_id'] # Clean up session
            return redirect('dashboard')
        else:
            return render(request, 'verify.html', {'error': 'Invalid or expired OTP'})
            
    return render(request, 'accounts/verify.html')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
