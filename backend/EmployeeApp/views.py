from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from EmployeeApp.models import Department,Employee
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

#
# FUNCTION BASED VIEW
#
@csrf_exempt
def departmentApi(request,id=None):
    if request.method=='GET':
        departments=Department.objects.all()
        department_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(department_serializer.data,safe=False)
    

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Data save sucessfully!!!",safe=False)
        return JsonResponse("Fail to add Data!!!",safe=False)
    

    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    

    elif request.method == 'DELETE':
        if id is not None:
            try:
                department = Department.objects.get(DepartmentId=id)
                department.delete()
                return JsonResponse("Deleted Successfully!!", safe=False)
            except Department.DoesNotExist:
                return JsonResponse("Department not found", safe=False, status=404)
        else:
            return JsonResponse("ID not provided", safe=False, status=400)
    else:
        return JsonResponse("Invalid request method", safe=False, status=400)
    


@csrf_exempt
def EmployeeApi(request,id=None):
    if request.method=='GET':
        employee=Employee.objects.all()
        employee_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Data save sucessfully!!!",safe=False)
        return JsonResponse("Fail to add Data!!!",safe=False)
    

    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    

    elif request.method == 'DELETE':
        if id is not None:
            try:
                employee = Employee.objects.get(EmployeeId=id)
                employee.delete()
                return JsonResponse("Deleted Successfully!!", safe=False)
            except Employee.DoesNotExist:
                return JsonResponse("Department not found", safe=False, status=404)
        else:
            return JsonResponse("ID not provided", safe=False, status=400)
    else:
        return JsonResponse("Invalid request method", safe=False, status=400)
    
@csrf_exempt
def SaveFile(request):
    file=request.FILES['myfiles']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
    