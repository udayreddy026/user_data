from django.shortcuts import render,redirect
from .models import user

# Create method API
def create(request):
    if request.method == "POST":
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        dob = request.POST['dob']
        location = request.POST['location']
        id = None
        obj = user(id,first,last,email,dob,location)
        obj.save()
        return redirect('/')
   
# Read method API
def read(request):
    try:
        obj = user.objects.all()
    except user.DoesNotExist:
        obj = None
    return render(request,'index.html',{'key':obj})

# Update method API
def update(request,id):
    if request.method == "POST":
        first_name = request.POST['first']
        last_name = request.POST['last']
        email = request.POST['email']
        dob = request.POST['dob']
        location = request.POST['location']

        obj1 = user.objects.get(id=id)
        obj1.first = first_name
        obj1.last = last_name
        obj1.email = email
        obj1.dob = dob
        obj1.location = location
        obj1.save()
        
        return redirect('/')
    else:
        try:
            obj = user.objects.get(id=id)
        except user.DoesNotExist:
            obj = None

        return render(request,'edit.html',{'key':obj})

# Delete method API
def delete(request,id):
    try:
        obj = user.objects.get(id=id)
    except user.DoesNotExist:
        obj = None
    
    obj.delete()
    return redirect('/')
