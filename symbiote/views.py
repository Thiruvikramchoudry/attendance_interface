from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import details,attendence_area,absenteism_count
import datetime,json
import pandas as pd
import os


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
    record=absenteism_count.objects.all()
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


def add_employee(request):
    if request.method=="POST":
        name=request.POST['name']
        designation=request.POST['designation']
        date_of_birth=request.POST['date_of_birth']
        gender= request.POST['gender']
        address = request.POST['address']
        phone=request.POST['phone_number']
        image = request.POST.get("image")
        # emp=details(name=name,designation=designation,date_of_birth=date_of_birth,gender=gender,address=address,phone=phone)
        # emp.save()
        print(name,designation,date_of_birth,gender,address,phone,image)
        return redirect('sample')
    return render(request,'symbiote/add_employee.html',{'username':"sample"})



def save_excel(request):
    employee=details.objects.all()
    emp_id=[]
    for i in employee:
        emp_id.append(i.Employee_id)
    today_status=attendence_area.objects.filter(Date=datetime.date.today())
    late_entry=[];present=[]
    for i in today_status:
        time=i.Time
        time = str((time)).split(":")
        hh = int(time[0])
        mm = int(time[1])
        ss = int(time[2])
        if hh > 10 or (hh == 10 and mm != 0):
            late_entry.append(i.Employee_id)
        else:
            present.append(i.Employee_id)
    lateandpresent=present+late_entry
    absent_entry=set(emp_id)-set(lateandpresent)
    status=[]
    for i in emp_id:
        if i in late_entry:
            status.append([i,"Late"])
        elif i in present:
            status.append([i,"present"])
        elif i in absent_entry:
            status.append([i,"absent"])

    print(status)
    df = pd.DataFrame(status, columns=['Employee_Id', 'Status'])
    date=datetime.datetime.today().date()
    df.to_excel("symbiote/static/symbiote/index_styles/attendance_status_files/"+(str(date) + ".xlsx"))
    return redirect('sample')

def save_clear(request):
    employee = details.objects.all()
    emp_id = []
    for i in employee:
        emp_id.append(i.Employee_id)
    today_status = attendence_area.objects.filter(Date=datetime.date.today())
    late_entry = []
    present = []
    for i in today_status:
        time = i.Time
        time = str((time)).split(":")
        hh = int(time[0])
        mm = int(time[1])
        ss = int(time[2])
        if hh > 10 or (hh == 10 and mm != 0):
            late_entry.append(i.Employee_id)
        else:
            present.append(i.Employee_id)
    lateandpresent = present + late_entry
    absent_entry = set(emp_id) - set(lateandpresent)
    status = []
    for i in emp_id:
        if i in late_entry:
            status.append([i, "Late"])
        elif i in present:
            status.append([i, "present"])
        elif i in absent_entry:
            status.append([i, "absent"])

    print(status)
    df = pd.DataFrame(status, columns=['Employee_Id', 'Status'])
    date=datetime.datetime.today().date()
    df.to_excel("symbiote/static/symbiote/index_styles/attendance_status_files/"+(str(date) + ".xlsx"))
    clear(request)


def download_stats(request):
    dir_list = os.listdir('symbiote/static/symbiote/index_styles/attendance_status_files')
    for i in range(len(dir_list)):
        dir_list[i]=dir_list[i].split(".")[0]

    return render(request,'symbiote/download_files.html',{"username":"sample","files_dir":dir_list})

def login2(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        password=request.POST['password']
        print(user_name,password)
        return redirect('login2')
    return render(request,'symbiote/login2.html')











    



