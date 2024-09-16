from django.shortcuts import render , HttpResponse ,redirect

# Create your views here.

def hello(request) :
  return render(request , 'index.html')

  