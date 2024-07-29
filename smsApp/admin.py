from django.contrib import admin
from .models import Student, Employee, Donor, School
# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Donor)
admin.site.register(School)