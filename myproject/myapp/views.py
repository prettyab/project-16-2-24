# Create your views here.
# employee/views.py



from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login as auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        # Username verification
        if User.objects.filter(email=email).exists():
            messages.info(request, "already exist")
            return redirect('register')
              
        # Create a new user
        user = User.objects.create_user(username=email,email=email,password=password)
        user.username=email 
        user.save() 
        messages.success(request, "Registration successful. You can now log in.")
        return redirect(reverse('login_view'))

    else:
        return render(request, 'register.html')

from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib import messages, auth
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib import messages, auth

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email, password=password)

        if user is not None:
            auth(request, user)
            request.session['user_id']=user.id
            request.session['user_email']=user.email
            return redirect('home2')
        
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login_view')

    return render(request, 'loggin.html')


  # Fix the template name to 'login.html'



  # Adjust the redirect to match your URL pattern

    

###REdirect PAge###
def home2(request):
    return render(request,'home2.html')

##MAIN PAGE###
def homee_view(request):
    return render(request,'homee.html')






# Replace 'homee.html' with your actual template
