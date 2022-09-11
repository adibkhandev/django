from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
# Create your views here.
def home(request):
    return render(request,"index.html")


def reg(request):
    if request.method == "POST" :
       username = request.POST['username']
       firstname = request.POST['firstname']
       password = request.POST["password1"]
       email = request.POST["email"]
       user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname)
       user.save();
       return redirect('/')
       print('user')
 
    else:
       return render(request,"reg.html")    


def login(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        

        user = auth.authenticate(username=username,password=password)
        

        if user is not None:
             
         
             return redirect('/')
            

        else:
           
            return redirect('login/')
           
    else:
        return render(request,"login.html")    


def products(resuest):
     return render(request,"products.html")        