from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from .forms import *
from django.contrib.auth import authenticate, login
from django.http.request import QueryDict
from datetime import date, datetime, timedelta
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# Create your views here.


# hr can able to create employee

def employee_create(request):
    user = request.session['obj']
    hr = Employee.objects.filter(active_flag=True, id=user, role='hr')
    if hr:
        if request.POST:
            data = QueryDict.dict(request.POST)
            today = date.today()
            d1 = today.strftime("%y")
            data['date_of_joining'] = date.today()
            form = EmployeeCreateform(data=data)
            if form.is_valid():
                form_obj = form.save()
                print(form_obj, 'pppppppppp', type(form_obj))
                password = data.pop('password')
                form_obj.set_password(password)
                form_obj.save()
                print('sdfghcvb')
                emp = Employee.objects.get(pk=form_obj.id)
                print(d1, type(d1))
                emp.employee_id = 'APPY' + '/' + d1 + '/' + str(emp.id)
                emp.save()
            else:
                return JsonResponse(form.errors)

        template = 'signup.html'
        form = EmployeeDisplayform()
        return render(request, template, {'form': form})
    else:
        return HttpResponse({"no permission"})


def employee_login(request):
    if request.POST:
        if request.POST:
            employee_id = request.POST['employee_id']
            password = request.POST['password']
            obj = Employee.objects.get(active_flag=True, employee_id=employee_id)
            print(obj.check_password(password))
            if obj.check_password(password):
                request.session["obj"] = obj.id
                print(obj.role)
                # if obj.role == 'hr':
                return redirect(homepage)
                # print(request.session)
                #     return render(request, 'homepage_hr.html')


            else:
                 return JsonResponse({'message': 'Invalid username or password'})
    form = Employeeloginform()
    template = 'login.html'
    context = {'form': form}
    return render(request, template, context)



# # @user_passes_test(lambda u:u.is_active)

# def hr_homepage(request):
#     return render(request, 'hr_homepage.html')

def homepage(request):
    user = request.session['obj']
    print(user)
    obj = Employee.objects.get(active_flag=True, id = user)
    print(obj.role)
    if obj.role == 'hr':
        return render(request, 'homepage_hr.html')
    elif obj.role == 'su':
        return render(request, 'homepage_admin.html')
    elif obj.role == 'manager':
        return render(request, 'homepage_manager.html')
    elif obj.role == 'lead':
        return render(request, 'homepage_lead.html')
    else:
        return render(request, 'homepage.html')




# # @user_passes_test(lambda u:u.is_staff)
# def staff(request):
#     # return render(request, 'homepage.html')
#     return HttpResponse("Hi STAFF")
#
# @user_passes_test(lambda u:u.is_superuser)
# def superuser(request):
#     # return render(request, 'homepage.html')
#     return HttpResponse("Hi Super")


# def logout(request):
# 	if request.session.is_authenticated():
# 		auth.logout(request)
# 		messages.success(request, 'Successfully logged out.')
# 	return HttpResponseRedirect(reverse('login'))



def logout(request):
    try:
        del request.session['obj']
        logout(request)

    except KeyError:
        pass
    return HttpResponseRedirect('/login')



def list_all_employee(request):
    user = request.session['obj']
    print(user)
    obj = Employee.objects.filter(active_flag=True)
    return render(request, 'list_employee.html', {'obj': obj})


def search_employee(request):
    all = Employee.objects.filter(active_flag=True)

    if ('q' in request.GET) and request.GET['q'].strip():
        search = request.GET.get('q')
        search_obj = Employee.objects.filter(Q(full_name__icontains=search)| (Q(employee_id__icontains=search)))
    else:
        search_obj = all
        # return render(request, 'search_directory.html', {'all':all})
    return render(request, 'search_directory.html', {'search_obj': search_obj, 'all':all})



def all_employee(request):
    user = request.session['obj']
    print(user)
    obj = Employee.objects.filter(active_flag=True)
    return render(request, 'all_employee.html', {'obj': obj})


def updatebankdetails(request, pk):
    obj = Employee.objects.get(pk=pk)
    print(obj, 'asdad')
    if request.POST:
        data = QueryDict.dict(request.POST)
        # user = request.session['obj']
        # emp = Employee.objects.get(active_flag=True, employee_id=obj.employee_id)
        # print(emp.employee_id)
        data['user'] = obj.id
        print(data)
        form = Bankdetailsform(data=data)
        if form.is_valid():
            form.save()
            return HttpResponse({'submitted'})
        return JsonResponse(form.errors)
    form = BankDisplayform()
    return render(request, 'add_bank_details.html', {'form': form})
    # return redirect(bankcreate)


def updatepfdetails(request, pk):
    obj = Employee.objects.get(pk=pk)
    print(obj.employee_id, 'pf')
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        # emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = obj.employee_id
        # print(data['user'])
        form = PFdetailsform(data=data)
        if form.is_valid():
            print(form)
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = PFdisplayform()
    return render(request, 'add_pf_details.html', {'form': form})




def updatequalificationdetails(request, pk):
    obj = Employee.objects.get(pk=pk)

    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        # emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = obj
        print(data)
        form = Qualificationcreateform(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = QualificationDisplayform()
    return render(request, 'add_qualification.html', {'form': form})


# def hr_bank_update(request):
#     if request.POST:
#         data = QueryDict.dict(request.POST)
#         # user = request.session['obj']
#         # emp = Employee.objects.get(active_flag=True, employee_id=user)
#         # data['user'] = user
#         print(data)
#         form = Bankdetailsform(data=data)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'submitted'})
#         return JsonResponse(form.errors)
#     form = BankDisplayform()
#     return render(request, 'add_bank_details.html', {'form': form})



def bankcreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = user
        print(data)
        form = Bankdetailsform(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = BankDisplayform()
    return render(request, 'add_bank_details.html', {'form': form})


def qualificationcreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = user
        print(data)
        form = Qualificationcreateform(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = QualificationDisplayform()
    return render(request, 'add_qualification.html', {'form': form})



def pfdetails(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = emp.id
        print(data['user'])
        form = PFdetailsform(data=data)
        if form.is_valid():
            print(form)
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = PFdisplayform()
    return render(request, 'add_pf_details.html', {'form': form})



def resignationcreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = emp.id
        data['submitted_on'] = date.today()
        form = ResignationCreateForm(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)

    form = ResignationDisplayForm()
    return render(request, 'resignation.html', {'form': form})



def careerinfocreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = emp.id
        print(data['user'])
        form =  CareerinfoCreateform(data=data)
        if form.is_valid():
            print(form)
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = CareerinfoDisplayform()
    return render(request, 'add_career_info.html', {'form': form})

def employeehistorycreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = emp.id
        print(data['user'])
        form = EmployeeHistoryCreateform(data=data)
        if form.is_valid():
            print(form)
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = EmployeeHistoryDisplayform()
    return render(request, 'add_employee_history.html', {'form': form})


def familydetailscreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        emp = Employee.objects.get(active_flag=True, employee_id=user)
        data['user'] = emp.id
        print(data['user'])
        form = FamilydetailsCreateForm(data=data)
        if form.is_valid():
            print(form)
            form.save()
            return JsonResponse({'message': 'submitted'})
        return JsonResponse(form.errors)
    form = FamilydetailsDisplayForm()
    return render(request, 'add_familydetails.html', {'form': form})



def employee_information(request):
    user = request.session['obj']
    emp_id = get_object_or_404(Employee, id=user)
    print(emp_id.employee_id)
    basic_info = Employee.objects.filter(employee_id = emp_id.employee_id)
    bank = Bankdetails.objects.filter(user=emp_id)
    pf = PFdetails.objects.filter(user=emp_id)
    qualification = Qualificationdetails.objects.filter(user=emp_id)
    resignation = Resignation.objects.filter(user=emp_id)
    career = Careerinfo.objects.filter(user=emp_id)
    history = EmployeeHistory.objects.filter(user=emp_id)
    family = Familydetails.objects.filter(user=emp_id)
    context = { 'basic_info' : basic_info, 'bank':bank, 'pf':pf, 'qualification': qualification, 'resignation': resignation, 'career': career, 'history':history, 'family': family}
    return render(request, 'employee_information.html', context)

def change_password(request):
    """ change password"""

    user = request.session['obj']
    data = QueryDict.dict(request.POST)
    obj = get_object_or_404(Employee, active_flag=True, id=user)
    print(obj.employee_id)
    if request.POST:
        form = Changepasswordform(data=data)
        if form.is_valid():
            print(form['password'])
            if obj.check_password(data['password']):
                new_password = data['new_password']
                re_enter_new_password = data['re_enter_new_password']
                if new_password == re_enter_new_password:
                    obj.password = new_password
                    obj.set_password(obj.password)
                    obj.save()
                    return JsonResponse({'message': "password changed"})
                else:
                    return JsonResponse({'message': 'new password and confirm new password doesn\'t match'})
            else:
                return JsonResponse({'message': 'Please enter old password correctly'})
    form = Changepasswordform()
    return render(request, 'changepassword.html', {'form': form})


# def change_password(request):
#     if request.method == 'POST':
#         user = request.session['obj']
#         print(user)
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was updated successfully!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'changepassword.html', {
#         'form': form
#     })


def check_status(request):
    user = request.session['obj']
    print(user)
    time_threshold = datetime.now() - timedelta(days=180)
    today = date.today()
    emp_list = Employee.objects.filter(active_flag=True, date_of_joining__lt=time_threshold, emp_status='pp')
    return render(request, 'check_status.html', {'emp_list': emp_list})

def change_status(request,pk):
    status = Employee.objects.get(pk=pk)
    status.emp_status = "cn"
    status.save()
    return redirect(check_status)


def assign_lead(request):
    user = request.session['obj']
    # print(user)
    role = Employee.objects.filter(active_flag=True, employee_id=user, role='hr')
    obj = Employee.objects.filter(active_flag=True, role='dev')
    lead = Employee.objects.filter(active_flag=True, role='lead')
    if role:
        print(role)
        # return redirect(select_employee_lead)
    form = Assignleadform()
    return render(request, 'assign_lead.html', {'obj': obj, 'lead': lead, 'form': form})

def select_employee_lead(request, pk):
    print('hi')
    obj = Employee.objects.get(pk=pk)
    print(obj)
    lead = Employee.objects.filter(active_flag=True, role='lead')

    print(lead)
    obj.reporting_lead = str(lead[1])
    # return render(request, 'assign_lead.html', {'obj': obj})
    obj.save()
    return redirect(assign_lead)
#     return HttpResponse("Thnkyou {}".format(pk))




# def select_employee_lead(request, pk):
#     return HttpResponse("Thnkyou {}".format(pk))

# def reporting_lead(request, pk):
#     print('jhcxcz')
#     lead = Employee.objects.filter(active_flag=True, role='lead', pk=pk)
#     print(lead)
#     # return render(request, 'assign_lead.html', {'lead': lead})
#     return redirect(assign_lead)
    # return render(request, 'assign_lead.html')


def resignation_list(request):
    user = request.session['obj']
    # try:
    obj = Employee.objects.get(active_flag=True, id=user, role = 'hr')
    if obj:
        list = Resignation.objects.filter(active_flag=True)
        return render(request, 'resignation_list.html', {'list': list})
    else:
        return HttpResponse({"no perission"})
    # except:
    #     return HttpResponse({})


def resignation_apply(request, pk):
    obj = Resignation.objects.get(pk=pk)
    obj.active_flag = False
    obj.save()
    emp_id = obj.user.employee_id
    emp = Employee.objects.get(employee_id = emp_id)
    print(emp.employee_id)
    emp.active_flag = False
    emp.save()
    return redirect(resignation_list)