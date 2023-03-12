from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import details,attendence_area,absenteeism_count
import datetime,json

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
    record=absenteeism_count.objects.all()
    present_count=[];total_person=[];late_person=[];preleave_person=[];dates=[]
    for i in record[::-1][:6][::-1]:
        present_count.append(i.Total_person-i.preleave_count-i.absent_count)
        total_person.append(i.Total_person)
        late_person.append(i.late_count)
        preleave_person.append(i.preleave_count)
        dates.append(i.Date)


    return render(request, 'symbiote/index.html', {'username': "sample", 'details': data,'total_count':total_count,'today_count':today_count,'late_entry':late_entry,'present_count':present_count,'total_person':total_person,'late_person':late_person,'preleave_person':preleave_person,'dates':dates})



def clear(request):
    data=attendence_area.objects.all()
    data.delete()
    return redirect('sample')

def employee_detail(request):
    Employee_data=details.objects.all()
    return render(request,'symbiote/employee_details.html',{'username':'sample','details':Employee_data})


def attendance_status(request):
    data = attendence_area.objects.all()
    return render(request,'symbiote/attendance_status.html',{'username': "sample", 'details': data})
