from django.shortcuts import render,HttpResponse,redirect
from .models import * 
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request,message=None):
    if message is not None:
        context={'message':message}
    else:
        context={}
    return render(request,'uniqueid.html',context)
def pwd(request):
    try:
        if request.method=="GET":
            user_name=request.GET.get('uniqueid','')
            
            user=User.objects.get(username=user_name)
            print(user_name)
            full_name=user.get_full_name()
            #email=User.email
            ud=UserDetails.objects.get(user=user)
            dob=ud.date_of_birth
            gender=ud.gender
            context={'full_name':full_name,'dob':dob,'gender':gender,'user':user,'user_details':ud}
            #print(full_name,dob,gender)
        return render(request,'welcome.html',context)
    except:
        return index(request)
def login_view(request):
    if request.method=="POST":
        print("done")
        username=request.POST.get('username',None)
        passwd=request.POST.get('password',None)
        print(username,passwd)
        if (username and passwd):
            user= authenticate(username=username,password=passwd)
            if user is not None:
                login(request,user)
                return download_docs(request)
            else:
                user=User.objects.get(username=username)
                full_name=user.get_full_name()
                #email=User.email
                ud=UserDetails.objects.get(user=user)
                dob=ud.date_of_birth
                gender=ud.gender
                context={'full_name':full_name,'dob':dob,'gender':gender,'user':user,'msg':"invalid credencials"}
                #context={"msg":"Invalid Credencials","user":user}
                return render(request,'welcome.html',context)    
    return HttpResponse("error")
def logout_view(request):
    logout(request)
    return redirect('home')
def download_docs(request):
    if request.user.is_authenticated:
        docs=documents.objects.filter(user=request.user)
        for d in docs:
            print(d.document_name)
        context={'docs':docs}
        return render(request,'download.html',context)
    else:
        return HttpResponse("Please Login First!!!")