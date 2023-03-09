from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import details,attendence_area
import datetime

# Create your views here.

def main(request):
    return render(request,'symbiote/login.html')


def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        data=attendence_area.objects.all()[:5]
        return render(request,'symbiote/index.html',{'username':username,'details':data})
    return redirect('/')


def sample(request):
    data = attendence_area.objects.all()[:5]
    total_count=len(details.objects.all())
    date=datetime.date.today()
    today_count=len(attendence_area.objects.filter(Date=date))
    today_emp=attendence_area.objects.filter(Date=date)
    late_entry=0
    for i in today_emp:
        time=str((i.Time)).split(":")
        print(time)
        hh=int(time[0])
        mm=int(time[1])
        ss=int(time[2])
        if hh>10 or (hh==10 and mm!=00 ):
            late_entry+=1


    return render(request, 'symbiote/index.html', {'username': "sample", 'details': data,'total_count':total_count,'today_count':today_count,'late_entry':late_entry})



def clear(request):
    data=attendence_area.objects.all()
    data.delete()
    return redirect('sample')

def employee_detail(request):
    Employee_data=details.objects.all()
    return render(request,'symbiote/detail_page.html',{'Employee_data':Employee_data})
