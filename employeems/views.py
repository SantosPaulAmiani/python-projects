from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin  # You'll need to define an Admin model in your Django app

def add_admin(request):
    if not request.session.get('alogin'):
        return redirect('index')

    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        # You'll need to create a Django Admin model and use it here to insert data into the database
        admin = Admin(fullname=fullname, email=email, password=password, username=username)
        admin.save()
        messages.success(request, 'New admin has been added successfully')

    return render(request, 'add_admin.html')
