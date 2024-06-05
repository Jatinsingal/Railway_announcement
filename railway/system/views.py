from django.shortcuts import render, HttpResponse
from datetime import datetime
from system.models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html',{'link' : 'index.html' ,})

def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request, 'index1.html')

def homebtn(request):
    return render(request, 'homebtn.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 