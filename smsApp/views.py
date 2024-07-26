from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentForm, EmployeeForm
from .models import Student, Employee
from .filters import StudentFilter, EmployeeFilter
# Create your views here.

def HomeView(request):
    return render(request, 'index.html')

def LoginView(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dataentry')
        else:
            messages.info(request, 'USERNAME or PASSWORD is incorrect!')
    return render(request, 'login.html')

def DataEntryView(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'dataentry.html',{'students':students})
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Successfully added!")
            return redirect('student_list')
        else:
            return render(request, 'add_student.html', {'form':form})

    form = StudentForm()
    return render(request, 'add_student.html',{'form':form})
def student_list(request):
    students = Student.objects.all().order_by('id')
    myFilter = StudentFilter(request.POST, queryset=students)
    students = myFilter.qs
    context ={'students':students, 'myFilter':myFilter}
    return render(request, 'student_list.html', context)
def EditStudentView(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.info(request, 'Changes Saved Successfully!')
            return redirect('student_list')
    context={'form':form}
    return render(request, 'add_student.html', context)
def DeleteStudentView(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.info(request, "Student Successfully Deleted!")
        return redirect('dataentry')
    context ={'student': student}    
    return render(request, 'delete.html', context)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Successfully Added!')
            return redirect('employee_list')
        else:
            return render(request, 'add_employee.html', {'form': form})
    form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    myFilter = EmployeeFilter(request.POST, queryset=employees)
    employees = myFilter.qs
    context = {'employees':employees, 'myFilter':myFilter}
    return render(request, 'employee_list.html', context)
def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form= EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect('employee_list')
        
    context = {'form': form}
    return render(request, 'add_employee.html', context)
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "Employee Successfully deleted!")
        return redirect('employee_list')
    context = {'employee': employee}
    return render(request, 'employee_delete.html', context)

def LogoutView(request):
    logout(request)
    return redirect('Home')