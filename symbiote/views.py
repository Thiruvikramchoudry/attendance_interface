from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
# from .models import details,attendence_area,absenteism_count
from .models import supervisor_detail, supervisor_assign, project, employee_details, employee_assign
import datetime
import pandas as pd
# import symbiote.main_db_connection as mdb
from symbiote.svm_face_recognation.datasetCreation import VideoCamera, imageCapture
from django.http import StreamingHttpResponse
from symbiote.svm_face_recognation.videocapture import Video , datacreation , lis , refresh


# Create your views here.

def index(request):
    return render(request, 'symbiote/home_page.html')


def main(request):
    project_id = supervisor_assign.objects.get(supervisor_username=request.user).project_id
    employee_count = project.objects.get(project_id=project_id).employee_required
    today = datetime.date.today()

    file_name = (str(today.day) + '-' + str(
        today.month if len(str(today.month)) == 2 else '0' + str(today.month)) + '-' + str(today.year)) + ".xlsx"
    df = pd.read_excel(r'symbiote/employee_assign/' + str(project_id) + '/' + file_name)
    emp_id = df['Employee_id']
    try:
        status = df['Status'].value_counts()[True]
    except:
        status = 0
    detail_name = df['Employee_name']
    detail_status = df['Status']
    details = []
    for i in range(min(5, len(detail_name))):
        details.append([emp_id[i], detail_name[i], detail_status[i]])

    return render(request, 'symbiote/index.html',
                  {'username': request.user, 'employee_count': employee_count, 'present_count': status,
                   'details': details})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/admin_page')
        else:
            return render(request, 'symbiote/login.html', {'message': "Invalid credientials"})
    else:
        return render(request, 'symbiote/login.html', {'message': ""})


def admin_page(request):
    supervisor_count = len(supervisor_detail.objects.all())
    project_count = len(project.objects.all())
    employee_count = len(employee_details.objects.all())
    employee_required = 0
    for i in project.objects.all():
        employee_required += int(i.employee_required)
    projects = project.objects.all()

    return render(request, 'symbiote/admin_page.html',
                  {"username": request.user, 'supervisor_count': supervisor_count, 'project_count': project_count,
                   'employee_required': employee_count - employee_required, 'total_employee': employee_count,
                   'projects': projects})


def project_details(request):
    projects = project.objects.all()
    return render(request, 'symbiote/project_details.html', {'username': request.user, 'projects': projects})


def employee_detail_all(request):
    details = employee_details.objects.all()

    return render(request, 'symbiote/employee_detail_all.html', {'details': details, 'username': request.user})


def new_project(request):
    supervisor = supervisor_detail.objects.all()
    supervisor_available = []
    for i in supervisor:
        if i.status == False:
            supervisor_available.append(i)
    employee_det = employee_details.objects.all()
    emp_id = []
    for i in employee_det:
        if len(employee_assign.objects.filter(employee_id=i.employee_id)) == 0:
            emp_id.append(i)

    if request.method == "POST":
        l=[]

        project_area = request.POST['project_area']
        employee_required = request.POST['employee_required']
        supervisor_name = request.POST['supervisor']

        if len(supervisor_detail.objects.filter(username=supervisor_name))==0:
            print("yes")
            return render(request, 'symbiote/new_project.html', {'username': request.user, 'supervisor_available': supervisor_available})

        phone_number = request.POST['phone_number']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        for i in project.objects.all():
            l.append(i.project_id)
        project_id = max(l) + 1 if l!=[] else 100000
        project1 = project.objects.create(project_id=project_id, project_area=project_area, employee_required=employee_required,supervisor=supervisor_name,phone_number=phone_number,from_date=from_date,to_date=to_date)
        project1.save()
        print(project_id, project_area, employee_required, supervisor, phone_number, from_date, to_date)
        user=supervisor_detail.objects.get(username=supervisor_name)
        user.status=True
        user.save()
        employee_list=request.POST['employee_list']
        employee_list=employee_list.split(',')
        today=datetime.date.today()
        data=[False]*len(employee_list)
        data2 = {'emp_id': employee_list,
                 str(from_date): data}
        df2 = pd.DataFrame(data2)
        df2.to_excel('symbiote/project_updates/'+str(project_id)+'.xlsx',index = False)
        for i in employee_list:
            detail=employee_details.objects.get(employee_id=i);
            detail.working_status=True
            detail.save()
            emp_ass=employee_assign(employee_id=i,project_id=project_id)
            emp_ass.save()

        supervisor_ass=supervisor_assign(project_id=project_id,supervisor_username=supervisor_name,employee_list='symbiote/project_updates/'+str(project_id))
        supervisor_ass.save()

        return render(request, 'symbiote/new_project.html', {'username': request.user,'supervisor_available':supervisor_available})
    else:
        return render(request, 'symbiote/new_project.html', {'username':request.user,'supervisor_available':supervisor_available,'emp_details':emp_id})


# def sample(request):
#     data = attendence_area.objects.all()[:5]
#     total_count=len(details.objects.all())
#     date=datetime.date.today()
#     today_count=len(attendence_area.objects.filter(date=date))
#     today_emp=attendence_area.objects.filter(date=date)
#     late_entry=0
#     for i in today_emp:
#         time=str((i.Time)).split(":")
#         print(time)
#         hh=int(time[0])
#         mm=int(time[1])
#         if hh>10 or (hh==10 and mm!=00 ):
#             late_entry+=1
#     record=absenteism_count.objects.all()
#     present_count=[];total_person=[];late_person=[];preleave_person=[];dates=[]
#     for i in record[::-1][:6][::-1]:
#         present_count.append(i.Total_person-i.preleave_count-i.absent_count)
#         total_person.append(i.Total_person)
#         late_person.append(i.late_count)
#         preleave_person.append(i.preleave_count)
#         dates.append(i.date)
#
#
#     return render(request, 'symbiote/index.html', {'username': request.user, 'details': data,'total_count':total_count,'today_count':today_count,'late_entry':late_entry,'present_count':present_count,'total_person':total_person,'late_person':late_person,'preleave_person':preleave_person,'dates':dates})
#
#
#
# def clear(request):
#     data=attendence_area.objects.all()
#     data.delete()
#     mdb.delete_attendence()
#     return redirect('/')

def employee_detail(request):
    project_id = supervisor_assign.objects.get(supervisor_username=request.user).project_id
    Employee_id = employee_assign.objects.filter(project_id=project_id)
    employee_detail = []
    for i in Employee_id:
        employee_detail.append(employee_details.objects.get(employee_id=i.employee_id))

    return render(request, 'symbiote/employee_details.html', {'username': request.user, 'details': employee_detail})


def attendance_status(request):
    project_id = supervisor_assign.objects.get(supervisor_username=request.user).project_id
    today = datetime.date.today()
    file_name = (str(today.day) + '-' + str(
        today.month if len(str(today.month)) == 2 else '0' + str(today.month)) + '-' + str(today.year)) + ".xlsx"
    df = pd.read_excel(r'symbiote/employee_assign/' + str(project_id) + '/' + file_name)
    emp_id = df['Employee_id']
    detail_name = df['Employee_name']
    detail_status = df['Status']
    details = []
    for i in range(len(detail_name)):
        details.append([emp_id[i], detail_name[i], detail_status[i]])
    return render(request, 'symbiote/attendance_status.html', {'username': request.user, 'details': details})


def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone_number']
        aadhar_number = request.POST['aadhar_number']
        # emp = employee_details(username=name, age=age, date_of_birth=date_of_birth, gender=gender, address=address,phone_number=phone, aadhar_number=aadhar_number)
        # emp.save()
        return render(request, 'symbiote/imagecreation.html')


    return render(request, 'symbiote/add_employee.html')


# def save_excel(request):
#     employee=details.objects.all()
#     emp_id=[]
#     for i in employee:
#         emp_id.append(i.Employee_id)
#     today_status=attendence_area.objects.filter(date=datetime.date.today())
#     late_entry=[];present=[]
#     for i in today_status:
#         time=i.Time
#         time = str((time)).split(":")
#         hh = int(time[0])
#         mm = int(time[1])
#
#         if hh > 10 or (hh == 10 and mm != 0):
#             late_entry.append(i.Employee_id)
#         else:
#             present.append(i.Employee_id)
#     lateandpresent=present+late_entry
#     absent_entry=set(emp_id)-set(lateandpresent)
#     status=[]
#     for i in emp_id:
#         if i in late_entry:
#             status.append([i,"Late"])
#         elif i in present:
#             status.append([i,"present"])
#         elif i in absent_entry:
#             status.append([i,"absent"])
#
#
#     #df = pd.DataFrame(status, columns=['Employee_Id', 'Status'])
#     date=datetime.datetime.today().date()
#     #df.to_excel("symbiote/static/symbiote/index_styles/attendance_status_files/"+(str(date) + ".xlsx"))
#     return redirect('sample')
#
# def save_clear(request):
#     print("yes")
#     employee = details.objects.all()
#     emp_id = []
#     for i in employee:
#         emp_id.append(i.Employee_id)
#     today_status = attendence_area.objects.filter(date=datetime.date.today())
#     late_entry = []
#     present = []
#     for i in today_status:
#         time = i.Time
#         time = str((time)).split(":")
#         hh = int(time[0])
#         mm = int(time[1])
#         if hh > 10 or (hh == 10 and mm != 0):
#             late_entry.append(i.Employee_id)
#         else:
#             present.append(i.Employee_id)
#     lateandpresent = present + late_entry
#     absent_entry = set(emp_id) - set(lateandpresent)
#     status = []
#     for i in emp_id:
#         if i in late_entry:
#             status.append([i, "Late"])
#         elif i in present:
#             status.append([i, "present"])
#         elif i in absent_entry:
#             status.append([i, "absent"])
#     print(status)
#
#
#     #df = pd.DataFrame(status, columns=['Employee_Id', 'Status'])
#     date=datetime.datetime.today().date()
#     #df.to_excel("symbiote/static/symbiote/index_styles/attendance_status_files/"+(str(date) + ".xlsx"))
#     data = attendence_area.objects.all()
#     data.delete()
#     return redirect('/')


def download_stats(request):
    return render(request, 'symbiote/download_files.html', {"username": request.user})


def video_feed(request):
    return StreamingHttpResponse(imageCapture(VideoCamera() , "Praveen" , 12), content_type='multipart/x-mixed-replace; boundary=frame')


def video_feed1(request):
    return StreamingHttpResponse(datacreation(Video()), content_type='multipart/x-mixed-replace; boundary=frame')

def stop_streaming1(request):
    if request.method == "POST":
        print("PRINTING")
        camera = Video()
        camera.stop_streaming()
        return render(request, 'symbiote/download_files.html', {"status": True, "username": request.user , "lis" : []})
    l = list(set(lis()))
    print(l)
    refresh()
    print(l)
    return render(request, 'symbiote/download_files.html', {"status": False, "username": request.user , "lis" : l})


def stop_streaming(request):
    if request.method == "POST":
        print("PRINTING")
        # camera = VideoCamera()
        # camera.stop_streaming()
        return render(request, 'symbiote/imagecreation.html', {"status": True, "username": request.user})
    return render(request, 'symbiote/home_page.html', {"status": False, "username": request.user})

def uncapture(request):
    if request.method == "POST":
        return redirect('stop_streaming1')

def uncapture1(request):
    if request.method == "POST":
        return redirect('stop_streaming')


def login2(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        print(user_name, password)

        return redirect('login2')
    return render(request, 'symbiote/login2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login_supervisor(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(supervisor_detail.objects.filter(username=username, password=password)) != 0:
                if len(supervisor_assign.objects.filter(supervisor_username=username)) != 0:
                    return redirect('supervisor_page')
                else:
                    return render(request, 'symbiote/no_assign.html', {'username': username})

            else:
                return render(request, 'symbiote/login2.html', {'message': 'Incorrect Credientials'})

        return render(request, 'symbiote/login2.html', {'message': 'Incorrect Credientials'})
    else:
        return render(request, 'symbiote/login2.html', {'message': ''})

def imagecreation(request):
    return render(request, 'symbiote/imagecreation.html')

def add_supervisor(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        supervisor_details=supervisor_detail(username=username,password=password,supervisor_name=name,status=False)
        supervisor_details.save()
        return redirect('admin_page')

    return render(request,'symbiote/add_supervisor.html',{'username':request.user})


def morning_update(request):
    if request.method=='POST':
        pass
    else:
        projects=project.objects.all()
        return render(request,'symbiote/morning_update.html',{'username':request.user,'projects':projects})

def closing_update(request):
    if request.method=='POST':
        pass
    else:
        projects=project.objects.all()
        return render(request,'symbiote/closing_update.html',{'username':request.user,'projects':projects})


def clear_project(request):
    if request.method=='POST':
        pass
    else:
        projects=project.objects.all()
        return render(request,'symbiote/closing_update.html',{'username':request.user,'projects':projects})


