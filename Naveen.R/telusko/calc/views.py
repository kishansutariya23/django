from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    # return render(request,'home.html') #as already templates is defined now just include inner files and folder of that template folder

    # for dynamic content
    return render(request,'home.html',{'name':"kishan"})