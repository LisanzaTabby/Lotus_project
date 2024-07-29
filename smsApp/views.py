from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentForm, EmployeeForm, DonorForm, SchoolForm
from .models import Student, Employee,Donor, School
from .filters import StudentFilter, EmployeeFilter, DonorFilter, SchoolFilter
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
    return render(request, 'deletion/student_delete.html', context)
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
    return render(request, 'deletion/employee_delete.html', context)

def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donor added successfully!')
            return redirect('donor_list')
        else:
            return render(request, 'add_donor.html', {'form':form})
        
    form = DonorForm()
    return render(request, 'add_donor.html', {'form':form})
def donor_list(request):
    donors = Donor.objects.all().order_by('id')
    myFilter = DonorFilter(request.POST, queryset=donors)
    donors = myFilter.qs
    context = {'donors': donors, 'myFilter': myFilter}
    return render(request, 'donor_list.html', context)
def edit_donor(request, pk):
    donor = Donor.objects.get(id=pk)
    form = DonorForm(instance=donor)
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Updated Successfully!')
            return redirect('donor_list')
    context = {'form':form}
    return render(request, 'add_donor.html', context)
def delete_donor(request, pk):
    donor = Donor.objects.get(id=pk)
    if request.method == 'POST':
        donor.delete()
        messages.success(request, 'Donor deleted Successfully!')
        return redirect('donor_list')
    
    context = {'donor':donor}
    return render(request, 'deletion/donor_delete.html', context)
def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            messages.success(request, 'School Added Successfully!')
            form.save()
            return redirect('school_list')
        else:
            return render(request, 'add_school.html', {'form':form})
    form = SchoolForm()
    return render (request, 'add_school.html', {'form':form})

def school_list(request):
    schools = School.objects.all().order_by('id')
    myFilter = SchoolFilter(request.POST, queryset = schools)
    schools = myFilter.qs
    context = {'schools':schools, 'myFilter':myFilter}
    return render(request, 'school_list.html', context)

def LogoutView(request):
    logout(request)
    return redirect('Home')