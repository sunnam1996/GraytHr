from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from employee.models import *
# from employee.views import *




# Create your views here.
# @user_passes_test(lambda u: u.is_superuser)
# def add_user(request):
#     form = AddUserForm(request.POST or None)
#     obj =  Employee.objects.filter(active_flag=True)
#     print(obj)
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save()
#             password = user.ph_no
#             user.set_password(password)
#             if user.Middle_name != '':
#                 user.name = '%s %s %s' % (user.Employee_first_name, user.Middle_name, user.Employee_last_name)
#             else:
#                 user.name = '%s %s' % (user.Employee_first_name, user.Employee_last_name)
#             user.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('add_user')
#         else:
#             messages.error(request, 'Failed')
#             form = AddUserForm()
#     return render(request, 'add_user.html', {'form': form, messages: form.errors})


# @user_passes_test(lambda u: u.is_superuser)
# def edit_user(request):
#     global edit_user
#     edit_user = ''
#     name_list = list(CustomUser.objects.exclude(emp_type='Admin').order_by('name').values_list('name', flat=True))
#     if request.method == 'POST':
#         edit_user = request.POST['name']
#         return redirect('edit_user_1')
#     return render(request, 'edit_user.html', {'name_list': name_list})


# @user_passes_test(lambda u: u.is_superuser)
# def edit_user_1(request):
#     obj_name = edit_user
#     obj = CustomUser.objects.get(name=obj_name)
#     form = EditUserForm(request.POST or None, instance=obj)
#     if request.method == 'POST':
#         import pdb;
#         pdb.set_trace()
#         if form.is_valid:
#             user = form.save()
#             if user.Middle_name != '':
#                 user.name = '%s %s %s' % (user.Employee_first_name, user.Middle_name, user.Employee_last_name)
#             else:
#                 user.name = '%s %s' % (user.Employee_first_name, user.Employee_last_name)
#             user.save()
#             users = CustomUser.objects.all()
#             for user in users:
#                 if user.user_status == 'Active':
#                     user.is_active = True
#                 else:
#                     user.is_active = False
#                 user.save()
#             messages.success(request, 'Data updated successfully')
#             return redirect('edit_user')
#     return render(request, 'edit_user_1.html', {'form': form})


# @user_passes_test(lambda u: u.is_superuser)
# def map_user(request):
#     # if manager changes to employee
#     check_id = list(Mapping.objects.all().values_list('Manager', flat=True))
#     for i in check_id:
#         check_obj = CustomUser.objects.get(id=i)
#         if check_obj.emp_type != 'Manager' or check_obj.user_status == 'Inactive':
#             del_obj = Mapping.objects.get(Manager=check_obj)
#             del_obj.delete()
#
#     # managers list
#     mngs = CustomUser.objects.filter(emp_type='Manager', user_status='Active')
#
#     # mng-emps dict
#     mng_dict = {}
#
#     for i in mngs:
#         try:
#             dict_obj = Mapping.objects.get(Manager=i)
#             emp_list = list(dict_obj.Employee.values_list('name', flat=True))
#             mng_dict[i] = emp_list
#         except:
#             pass
#     mng_dict_keys = mng_dict.keys()
#
#     # unmapped emps list
#     emp_list = list(CustomUser.objects.filter(emp_type='Employee'))
#     new = []
#     for i in emp_list:
#         try:
#             a = Mapping.objects.get(Employee=i)
#         except:
#             new.append(i.name)
#
#     if request.method == 'POST':
#         mng_name = request.POST['manager']
#         mng_obj = CustomUser.objects.get(name=mng_name)
#
#         # check if mng already present in mapping list or not
#         if mng_obj.id in check_id:
#             map_obj = Mapping.objects.get(Manager=mng_obj)
#         else:
#             map_obj = Mapping(Manager=mng_obj)
#             map_obj.save()
#         emp_names = dict(request.POST)['employee']
#         check_emp = list(Mapping.objects.all().values_list('Employee', flat=True))
#         for emp_name in emp_names:
#             emp_obj = CustomUser.objects.get(name=emp_name)
#             if emp_obj.id in check_emp:
#                 check_map = Mapping.objects.get(Employee=emp_obj)
#                 check_map.Employee.remove(emp_obj)
#             map_obj.Employee.add(emp_obj)
#         messages.success(request, 'Manager-Employee Registered')
#         return redirect('map_user')
#     return render(request, 'map.html', {'mngs': mngs, 'mng_dict': mng_dict, 'mng_dict_keys': mng_dict_keys, 'new': new})


# @login_required
def leave_request(request):
    # current_employee = request.employee.employee_id
    current_employee = request.session['obj']
    employee = Employee.objects.get(employee_id=current_employee)
    print(employee.reporting_lead)
    lead = Employee.objects.get(active_flag=True, pk=employee.reporting_lead, role = 'lead')
    print(lead.email)
    # try:
    #     is_emp_mapped = Mapping.objects.get(Employee=employee)
    # except:
    #     is_emp_mapped = False
    if request.method == 'POST':
        From = request.POST['From']
        print(From)
        To = request.POST['To']
        LeaveType = request.POST['LeaveType']
        Reason = request.POST['Reason']
        Fromsession = request.POST['Fromsession']
        Tosession = request.POST['Tosession']
        Days = To - From
        Balance_days = Days
        ApplyTo = request.POST['ApplyTo']
        Contact = request.POST['Contact']
        LeaveRequest.objects.create(employee=employee, From=From, LeaveType=LeaveType, To=To, Reason=Reason ,Fromsession=Fromsession,Tosession=Tosession,ApplyTo=ApplyTo,Contact=Contact,Days = Days,Balance_days = Balance_days)
        # try:
            # mng = Mapping.objects.get(Employee=employee).Manager
        # except:
        #     mng = employee
        messages.success(request, 'Leave request submitted successfully to %s' % lead.name)
        return redirect('leave_request')
    return render(request, 'request.html', {})


def history(request):
    current_employee = request.session['obj']
    employee = Employee.objects.get(employee_id=current_employee)
    if employee.current_employee == 'lead':
        return redirect('mng_history')
    else:
        return redirect('user_history')

def leavegrant(request):
    current_employee = request.session['obj']
    employee = Employee.objects.get(employee_id=current_employee)
    if employee.current_employee == 'reporting_lead':
        return redirect('mng_history')
    else:
        return redirect('user_history')

# @login_required
def mng_history(request):
    return render(request, 'mng_history.html')


# @login_required
def pending(request):
    current_employee= request.session['obj']
    user_obj =Employee.objects.get(employee_id=current_employee)
    try:
        lead = Employee.objects.filter(active_flag=True, role='lead')
        print(lead)
        map_obj = lead.objects.get(Manager=user_obj)
        emp_list = list(map_obj.Employee.values_list('name', flat=True))
    except:
        emp_list = []
    if emp_list == []:
        new_mng = True
    else:
        new_mng = False
    requests = LeaveRequest.objects.all()
    if request.method == 'POST':
        status = dict(request.POST)
        for i in status.keys():
            try:
                value = status[i]
                i = int(i)
                req_obj = LeaveRequest.objects.get(id=i)
                req_obj.Status = value[0]
                req_obj.save(update_fields=["Status"])
            except:
                pass
        return redirect('team_history')
    return render(request, 'pending.html', {'emp_list': emp_list, 'new_mng': new_mng, 'requests': requests})


def team_history(request):
    global emp_name
    emp_name = ''
    current_user = request.user.username
    user_obj = Employee.objects.get(username=current_user)
    try:
        map_obj = leave_request.objects.get(Lead=user_obj)
        emp_list = list(map_obj.Employee.values_list('name', flat=True))
    except:
        emp_list = []
    if emp_list == []:
        new_mng = True
    else:
        new_mng = False
    if request.method == 'POST':
        emp_name = request.POST['emp_name']
        return redirect('team_history_1')
    return render(request, 'team_history.html', {'emp_list': emp_list, 'new_mng': new_mng})


def team_history_1(request):
    employee = emp_type
    user_obj = Employee.objects.get(name=employee)
    requests = list(LeaveRequest.objects.filter(employee=user_obj).order_by('-From'))
    print(lead)
    if requests == []:
        requests = False
    return render(request, 'team_history_1.html', {'requests': requests})


def edit_history(request):
    current_employee= request.session['obj']
    user_obj = Employee.objects.get(employee_id=current_employee)
    requests = LeaveRequest.objects.filter(user=user_obj).order_by('-From')
    if request.method == 'POST':
        status = dict(request.POST)
        for i in status.keys():
            try:
                value = status[i]
                i = int(i)
                req_obj = LeaveRequest.objects.get(id=i)
                req_obj.Status = value[0]
                req_obj.save(update_fields=["Status"])
            except:
                pass
        return redirect('team_history_1')
    return render(request, 'edit_history.html', {'requests': requests})


def user_history(request):
    current_employee = request.session['obj']
    user_obj = Employee.objects.get(employee_id=current_employee)
    try:
        user_history = LeaveRequest.objects.filter(user=user_obj).order_by('-From')
        if list(user_history) == []:
            user_history = False
    except:
        user_history = False

    try:
        super_mng = LeaveRequest.objects.get(Employee=user_obj).Manager
    except:
        super_mng = True
    if request.method == 'POST':
        un = dict(request.POST).keys()
        for i in un:
            leave_id = i
        leave_obj = LeaveRequest.objects.get(id=int(leave_id))
        leave_obj.delete()
        return redirect('user_history')
    return render(request, 'user_history.html', {'user_history': user_history, 'super_mng': super_mng})


def leave_history(request):
    current_employee = request.session['obj']
    user_obj = Employee.objects.get(employee=current_employee)
    try:
        map_obj = Employee.objects.get(Manager=user_obj)
        emp_list = list(map_obj.Employee.values_list('name', flat=True))
    except:
        emp_list = []
    if emp_list == []:
        new_mng = True
    else:
        new_mng = False
    requests = LeaveRequest.objects.all()
    status_opts = ['Approve', 'Reject']
    return render(request, 'leave_history.html',
                  {'user_obj': user_obj, 'user_history': user_history, 'emp_list': emp_list, 'new_mng': new_mng,
                   'super_mng': super_mng, 'requests': requests, 'status_opts': status_opts})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was updated successfully!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {
        'form': form
    })
