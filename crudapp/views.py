from msilib.schema import ListView
from django.shortcuts import render,redirect
from . models import Crud
from django.contrib import messages

# Create your views here.





def add(request):
    crud1 = Crud.objects.all()
    if request.method == "POST":
        si = request.POST.get('si','')
        item = request.POST.get('item','')
        desc = request.POST.get('desc','')
        crud = Crud(si=si,item=item,desc=desc)
        crud.save()
        messages.success(request,"Data created successfully")
    return render(request,'index.html',{'crud1':crud1})

def delete(request,id):
    item = Crud.objects.get(id=id)
    item.delete()
    return redirect('/')

def update(request,id):
    crud2 = Crud.objects.get(id=id)
    if request.method == "POST":
        crud2.si = request.POST["si"]
        crud2.item = request.POST.get('item','')
        crud2.desc = request.POST.get('desc','')
        crud2.save()
        return redirect('/')
    return render(request,"update.html",{'crud2':crud2})
