from django.shortcuts import render,HttpResponse,redirect
from . models import Employee


# Create your views here.
def emphome(request):
    emp = Employee.objects.all()
    output = {'emp': emp}
    return render(request, 'emphome.html', output)


def reg(request):
    return render(request, 'reg.html')


def insert(request):
    empid = request.POST['empid']
    empname = request.POST['empname']
    address = request.POST['address']
    depertment = request.POST['depertment']
    salary = request.POST['salary']
    emp = Employee(empid=empid, empname=empname, address=address, depertment=depertment, salary=salary)
    print(emp)
    emp.save()
    return redirect('employee:emphome')
