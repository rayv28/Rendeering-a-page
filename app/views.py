from django.shortcuts import render

# Create your views here.
def fun(request):
  return render(request,'rev.html')