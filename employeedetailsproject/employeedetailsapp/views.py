from django.shortcuts import render, redirect
from .models import EmployeeDetails

def employeedata(request):
    if request.method == 'POST':
        empidentity1 = request.POST.get('empidentity')
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        sal1 = request.POST.get('sal')
        bonus1 = request.POST.get('bonus')
        dep1 = request.POST.get('dep')
        hdate1 = request.POST.get('hdate')
        pnumber1 = request.POST.get('pnumber')
        email1 = request.POST.get('email')

        data  = EmployeeDetails(
            emp_identity=empidentity1,
            first_name=fname1,
            last_name=lname1,
            salary=sal1,
            bonus=bonus1,
            department=dep1,
            hire_date=hdate1,
            phone_number=pnumber1,
            email=email1
        )
        data.save()
        employees = EmployeeDetails.objects.all()
        return render(request,'employee_details.html',{'employees':employees})
    else:
        employees = EmployeeDetails.objects.all()
        return render(request,'employee_details.html', {'employees':employees})

def update_employee_data(request,id):
    employees = EmployeeDetails.objects.get(id=id)
    return render(request, 'employee_data_updating.html', {'employees':employees})

def updated_data_save(request,id):
    if request.method == 'POST':
        employees = EmployeeDetails.objects.get(id=id)
        employees.emp_identity = request.POST.get('empidentity')
        employees.first_name = request.POST.get('fname')
        employees.last_name = request.POST.get('lname')
        employees.salary = request.POST.get('sal')
        employees.bonus = request.POST.get('bonus')
        employees.department = request.POST.get('dep')
        employees.hire_date = request.POST.get('hdate')
        employees.phone_number = request.POST.get('pnumber')
        employees.email = request.POST.get('email')
        employees.save()
        employees = EmployeeDetails.objects.all()
        return render(request,'employee_details.html',{'employees':employees})

def delete_employee_data(request, id):
    employees = EmployeeDetails.objects.get(id=id)
    employees.delete()
    return redirect('/')