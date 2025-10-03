from django.shortcuts import render,redirect
from . models import Contact
from . forms import Contactforms
from django.contrib import messages

def contactview(request):
    obj1=Contact.objects.all()
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        if Contact.objects.filter(email=email).exists():
                messages.error(request, "A contact with this email already exists.")
        elif Contact.objects.filter(phone=phone).exists():
                messages.error(request, "A contact with this phone number already exists.")
        else:
                obj=Contact(firstname=firstname,lastname=lastname,address=address,email=email,phone=phone)
                obj.save()
    
    return render(request,'contactview.html',{'obj1':obj1})


def delete(request,contactid):
    contact=Contact.objects.get(id=contactid)
    if request.method=="POST":
        contact.delete()
        return redirect('/')
    return render(request,'delete.html',{'contact':contact})


def update(request,id):
     contact=Contact.objects.get(id=id)
     form=Contactforms(request.POST or None,instance=contact)
     if form.is_valid():
         form.save()
         return redirect('/')
     return render(request,'edit.html',{'contact':contact,'form':form},)





