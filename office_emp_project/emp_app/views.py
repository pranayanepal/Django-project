from django.shortcuts import render,HttpResponse
from .models import Employes,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        new_emp=Employes(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('EMPLOYEE ADDED SUCCESSFULLY')
   
    elif request.method=='GET':
        return render(request,'add_employee.html')
    
    else:
        return HttpResponse('AN exception occured')

def remove_emp(request,emp_id=0):

    if emp_id:
        try:
            emp_to_be_removed=Employes.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("pls enter a valid id")

    emp=Employes.objects.all()
    context={
        'emps':emp
    }
    return render(request,'remove_employee.html',context)



def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        
        # Start with all employees
        emps = Employes.objects.all()

        # Apply filters conditionally
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_employee.html', context)
      
    elif request.method == 'GET':
        return render(request, 'filter_employee.html')
      
    else:
        return HttpResponse("An error occurred")

          
          

def view_emp(request):
    emp=Employes.objects.all()
    context={
        'emp':emp
    }
    print(context)
    return render(request,'view_employee.html',context)

