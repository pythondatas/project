from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    # messages.info(request,"logout successfully")
    return redirect('/')
def login(request):
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)

      if user is not None:
          auth.login(request,user)
          return redirect('/')
      else:
        messages.info(request,"Invalid Username or Password")
        return redirect('login')
   return render(request,"login.html")
def function2(request):
  if request.method=='POST':
     username=request.POST['uname']
     firstname=request.POST['fname']
     lastname=request.POST['lname']
     emailid= request.POST['email']
     pwd= request.POST['password']
     cpwd=request.POST['cpassword']
     if pwd==cpwd:
        if User.objects.filter(username=username).exists():
           messages.info(request,"username already exists")
           return redirect('register')
        elif User.objects.filter(email=emailid).exists():
            messages.info(request,"email already exist")
            return redirect('register')
        else:
           data=User.objects.create_user(username=username,password=pwd,first_name=firstname,last_name=lastname,email=emailid)
           data.save();
           return redirect('login')
           print("user created")

     else:
        messages.info(request,"check password")
        return redirect('register')
     return redirect('/')

  return render(request,"newpage.html")
