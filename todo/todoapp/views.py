from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoapp.models import Task

# Create your views here.

def home(request):

    return render(request,'home.html')



def delete(request,rid):

    #t1=Task.objects.get(id=rid)
    #print(t1)
    #t1.delete()
    t1=Task.objects.filter(id=rid)
    t1.update(is_deleted="Y")
    return redirect('/dashboard')


def index(request):

    return render(request,'index.html')

def dashboard(request):

    if request.method=="POST":

        t=request.POST['title']
        det=request.POST['detail']
        cat=request.POST['cat']
        dt=request.POST['date']
        #print(t)
        #print(det)
        #print(cat)
        #print(dt)
        t1=Task.objects.create(title=t,detail=det,cat=cat,date=dt,is_deleted='N')
        #print(t1)
        t1.save()

        return redirect('/dashboard')

    else:
        #records=Task.objects.all()
        #print(records)
        records=Task.objects.filter(is_deleted="N")
        content={}
        content['data']=records
        return render(request,'dashboard.html',content)


def edit(request,rid):
    if request.method=="POST":
        ut=request.POST['title']
        udet=request.POST['detail']
        ucat=request.POST['cat']
        udt=request.POST['date']
        #print(ut)
        #print(udet)
        #print(ucat)
        #print(udt)
        t1=Task.objects.filter(id=rid)
        t1.update(title=ut,detail=udet,cat=ucat,date=udt)
        return redirect("/dashboard")
    else:
        rec=Task.objects.filter(id=rid)
        content={}
        content['data']=rec
        return render(request,'editform.html',content)
