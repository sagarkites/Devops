from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Employees
from . serializers import employeeserializer

# Create your views here.
class employeeslist(APIView):

    def get(self, request):
        employees1 = Employees.objects.all()
        serialiazer=employeeserializer(employees1, many=True)
        return Response(serialiazer.data)
