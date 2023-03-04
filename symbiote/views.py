from django.shortcuts import render

from .models import details

# Create your views here.

def main(request):
    detail=details.objects.get(Employee_name="praveen")
    return render(request,'symbiote/login.html',{'status':detail.Status})

def click(request):
    detail=details.objects.get(Employee_name="praveen")
    detail.Status+=' p'
    detail.save()
    return render(request,'symbiote/index.html',{'status':detail.Status})
