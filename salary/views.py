from datetime import date, datetime, timedelta
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http.request import QueryDict

# Create your views here.



def salarycreate(request):
    if request.POST:
        data = QueryDict.dict(request.POST)
        user = request.session['obj']
        print(user)
        emp = Employee.objects.get(active_flag=True, employee_id=user, role='hr')

        if emp:
            form = SalaryCreateForm(data=data)
            data['user'] = user
            data['cost_to_company'] = int(data['cost_to_company'])
            data['basic_pay'] = ((data['cost_to_company']) * 40) / 100
            data['hra'] = ((int(data['basic_pay']) * 40) / 100)
            data['pf'] = ((int(data['basic_pay']) * 24) / 100)
            data['bonus'] = round(((data['basic_pay'] * 8.33) / 100),2)
            data['special_allowance'] = round((data['cost_to_company']) - (data['basic_pay'] + data['hra'] + data['pf']),2)
            data['monthly_basic_pay'] = round((data['basic_pay']) / 12 ,2)
            data['monthly_hra'] = round((data['hra']) / 12 ,2)
            data['monthly_pf'] = round((data['pf']) / 12 ,2)
            data['monthly_bonus'] = round((data['bonus']) / 12 ,2)
            data['monthly_special_allowance'] = round((data['special_allowance']) / 12 ,2)
            data['monthly_salary'] = data['monthly_basic_pay'] + data['monthly_hra'] + data['monthly_pf'] + data['monthly_bonus'] + data['monthly_special_allowance']
            print(data['monthly_salary'], type(data['monthly_salary']))
            print(data['monthly_special_allowance'], type(data['monthly_special_allowance']))

            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Submitted'})
            else:
                return JsonResponse(form.errors)
        else:
            return JsonResponse({'message': "no permission"})
    form = SalaryDisplayForm()
    return render(request, 'add_salary.html', {'form': form})



def salary_slip(request):
    user = request.session['obj']
    print(user)
    emp_id = Employee.objects.get(active_flag=True, id=user)
    print(emp_id.full_name)
    salary = Salarydetails.objects.filter(active_flag=True, emp_id=emp_id)
    # print(salary.user)
    emp = Employee.objects.filter(active_flag=True, id=user)
    print(emp)
    pf = PFdetails.objects.filter(active_flag=True, user=emp_id)
    print(pf)
    return render(request, 'salary_slip.html', {'salary': salary, 'pf': pf, 'emp': emp})


def employee_select(request):
    user = request.session['obj']
    hr = Employee.objects.get(active_flag=True, employee_id=user, role='hr')
    employee = Salarydetails.objects.filter(active_flag=True)
    print(employee)
    if hr:
        print(hr)
    return render(request, 'add_payslip.html', {'employee': employee})


def monthly_pay(request, pk):
    emp = get_object_or_404(Salarydetails, pk=pk)
    employee_id=emp.emp_id.employee_id
    print(emp.emp_id.id)
    sal = Salarydetails.objects.filter(pk=emp.id)
    # print(sal.monthly_basic_pay)
    if request.POST:
        data = QueryDict.dict(request.POST)
        data['emp_id'] = emp.emp_id.id
        data['basic_pay'] = emp.monthly_basic_pay
        data['hra'] = emp.monthly_hra
        data['bonus'] = emp.monthly_bonus
        data['special_allowance'] = emp.monthly_special_allowance
        data['pf'] = emp.monthly_pf
        data['esi'] = emp.monthly_esi
        data['earning'] = (float(data['basic_pay']) + float(data['hra']) + float(data['bonus']) + float(data['special_allowance']))
        data['deduction'] = (float(data['pf']) + float(data['esi']))
        data['total_income'] = (int(data['earning']) - int(data['deduction']))
        form = MonthlyslipForm(data=data)
        print(data['emp_id'])

        if form.is_valid():

            # data['emp_id'] = emp.emp_id.id
            form.save()
            return redirect(employee_select)
        else:
            return JsonResponse(form.errors)
    form = MonthlyslipDisplayForm()
    return render(request, 'add_payslip.html', {'sal':sal, 'form': form})

#
# def monthly_pay(request):
#     user = request.session['obj']
#     print(user)
#
#     if request.POST:
#         data = QueryDict.dict(request.POST)
#         hr = Employee.objects.get(active_flag=True, employee_id=user, role='hr')
#         employee = Salarydetails.objects.get(emp_id = data['emp_id'])
#         print(employee.hra, 'sdfds')
#
#         print(data['emp_id'])
#         if hr:
#             form = MonthlyslipForm(data=data)
#             # print(data['emp_id'])
#             data['earning'] = (float(data['basic_pay']) + float(data['hra']) + float(data['bonus']) + float(data['special_allowance']))
#             data['deduction'] = (float(data['pf']) + int(data['esi']))
#             data['total_income'] = data['earning'] - data['deduction']
#             if form.is_valid():
#                 form.save()
#                 return JsonResponse({'message': 'Submitted'})
#             else:
#                 return JsonResponse(form.errors)
#         else:
#             return JsonResponse({'message': "No permission"})
#     form = MonthlyslipDisplayForm()
#     return render(request, 'add_payslip.html', {'form': form})



def payslip(request):
    user = request.session['obj']
    emp = Employee.objects.get(active_flag=True, id=user)
    empl = MonthlySlip.objects.filter(emp_id=user)
    print(emp.employee_id)
    if emp:
        pay = MonthlySlip.objects.filter(active_flag=True, emp_id=emp)
        print(pay, 'assd')
    return render(request, 'payslip.html',{'pay': pay})

def pf_ytd_statement(request):
    user = request.session['obj']
    emp = Employee.objects.get(active_flag=True, id=user)

    print(emp.role)
    empl = MonthlySlip.objects.filter(emp_id=user)
    print(emp.employee_id)
    if emp:
        pay = MonthlySlip.objects.filter(active_flag=True, emp_id=emp)
        print(pay, 'assd')
        employee = Employee.objects.filter(active_flag=True, id=user)
        print(employee, 'lkjh')
        pf = PFdetails.objects.filter(active_flag=True, user=emp)
        print(pf)
    return render(request, 'pf_ytd.html', {'pay': pay, 'pf': pf, 'employee': employee})




def list_of_salary_employees(request):
    user = request.session['obj']
    emp = Employee.objects.get(active_flag=True, id=user)
    if emp.role == 'hr' or 'su':
        print(emp.role)
        sal = Salarydetails.objects.filter(active_flag=True)
        return render(request, 'salary_revision.html', {'sal': sal})
    else:
        return HttpResponse({"no permission"})


def salary_revision(request, pk):
    user = request.session['obj']
    emp = Employee.objects.get(active_flag=True, id=user)
    data = QueryDict.dict(request.POST)
    if emp.role == 'hr' or 'su':
        salary = Salarydetails.objects.get(pk=pk)
        print(salary)
        # print(sal.monthly_basic_pay)
        form = SalaryRevisionForm(data=data)
        # print(form['monthly_basic_pay'])
        print(form['per'])
        # percent = request.POST['percent']
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect(salary_revision)
            else:
                print(form.errors)

        form = SalaryRevisionDisplayForm()
        # print(form['per'])

        return render(request, 'salary_revision.html', {'form': form})
    else:
        return HttpResponse({"no perission"})