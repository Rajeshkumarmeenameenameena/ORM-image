from django.shortcuts import render,HttpResponse
from .form import studentform
from .models import *
# Create your views here.
def home(request):
    form1=student.objects.all()
    form=studentform()
    if request.method=='POST':
        stu=studentform(request.POST,request.FILES)
        print(stu)
        if stu.is_valid():
            stu.save()
    context={
        'form':form,
        'data':form1
    }
    return render(request,'app/home.html',context)

def studentdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        print(name,email,phoneno)
        mydata=student(name=name,email=email,phoneno=phoneno)
        mydata.save()
    return HttpResponse('submit form')

def file(request):
    if request.method=='POST':
        a=request.FILES['file']
        data=savefile.objects.create(file=a)
        data.save()
        print(a)
    return HttpResponse('savefile')

