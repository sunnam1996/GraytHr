from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from datetime import date, datetime
from .forms import *
from django.http.request import QueryDict

# Create your views here.


def leavetypecreate(request):
    form = Leavetypecreateform(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'leavetype.html', {'form': form})
    # return render(request, 'homepage.html')

def leaveapplycreate(request):
    if request.method=='POST':
        user = request.session['obj']
        data = QueryDict.dict(request.POST)
        form = Leaveapplyform(data)
        data['by'] = user
        if form.is_valid():
            obj = form.save(commit=False)
            d1 = datetime.strptime(data['to_date'], '%Y-%m-%d').date()
            d2 = datetime.strptime(data['from_date'], '%Y-%m-%d').date()
            delta = d1-d2
            obj.days = delta.days + 1
            obj.save()
            form.save()
            return HttpResponse('sunnam success')
    else:
        user = request.session['obj']
        lead_obj = Employee.objects.get(id=user)
        lead = lead_obj.reporting_lead
        lead_name = Employee.objects.get(id=lead)

        hr = Employee.objects.filter(role="hr").order_by('id')[0]
        superuser = Employee.objects.filter(role="su").order_by('id')[0]

        leads = {'lead': lead_name, 'hr': hr, 'superuser': superuser}
        form = Leaveapplyform(leads=leads)
        return render(request, 'leaveapply.html', {'form': form})


def leavecancel(request, pk):
    if request.method == 'POST':
        user = request.session['obj']
        obj = Leaveapply.objects.get(id=pk)
        if obj.active_flag:
            obj.active_flag = False
            obj.save()
        obj = Leaveapply.objects.filter(by=user, status=1, active_flag=True)
        return render(request, 'leavecancel_list.html', {'obj': obj})
    else:
        obj = Leaveapply.objects.get(id=pk)
        return render(request,'leavecancel.html',{'obj':obj})

def leavecancel_list(request):
    user = request.session['obj']
    list = Leaveapply.objects.filter(by=user,status=1,active_flag=True)
    return render(request, 'leavecancel_list.html', {'lists': list})


def leavetrack(request):
    user = request.session['obj']
    obj = Leaveapply.objects.filter(active_flag=True, by=user)
    return render(request, 'list_of_leave.html', {'obj': obj})


def assign_leavebalance(request):
    user = request.session['obj']
    print(user)
    # obj = Employee.objects.filter(active_flag=True, id=user)
    # print(obj)
    form = Leavebalanceform(request.POST)
    role = Employee.objects.filter(active_flag=True, role='hr', id=user)
    if role:
        print('as')
        if form.is_valid():
            form.save()
            form=Leavebalanceform
    return render(request, 'assign_leave.html', {'form':form})


def update_leavebalance(request, pk):
    user = request.session['obj']
    role = Employee.objects.filter(active_flag=True, role='hr', id=user)
    if role:
        update = get_object_or_404(Leavebalance, pk=pk)
        update.balance += 2
        update.save()
    return render(request, 'update_leave.html', {'update': update})


def leave_request_list(request):
    user = request.session['obj']
    role = Employee.objects.filter(active_flag=True, id=user, role='lead')
    list = Leaveapply.objects.filter(active_flag=True, apply_to=user)
    if role:
        return render(request, 'leave_request.html', {'list': list})
    return JsonResponse({'message': 'not lead'})


def leave_status(request, pk, status):
    # user = request.session['obj']
    # role = Employee.objects.filter(active_flag=True, id=user, role='lead')
    # list = Leaveapply.objects.filter(active_flag=True, pk=pk)
    # if list:
    #     if request.POST== '1':
    #         return JsonResponse({'message': 'reject'})
    #     else:
    #         return JsonResponse({'message': 'accept'})
    leave = Leaveapply.objects.get(pk=pk)
    leave.status = status
    leave.save()
    return render(request, 'leave_request.html', {'lists': leave})

def pending_requests(request):
    # if request.method=='POST':
    #     leave = Leaveapply.objects.filter(active_flag=True, pk=pk)
    #     leave.status = status
    user = request.session['obj']
    list = Leaveapply.objects.filter(active_flag=True, apply_to=user)
    return render(request,'pending_requests.html',{'lists':list})
