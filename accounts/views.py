from django.http import Http404
from .models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  RegisterUserSerializer, UserProfileSeralizer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.generics import CreateAPIView

from django.shortcuts import get_object_or_404
from .models import Attendance,Salary_table
from .serializers import AttendanceSerializer,AttendanceUpdateSerializer,EmployeeUpdateSerializer,Salary_tableSerializer,Leave_TableUpdateSerializer,Leave_TableSerializer
# import ValidationError from rest_framework.exceptions
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import EmployeeSerializer
from .authentication import create_access_tokken, create_refresh_tokken
from .models import Employee,Location,Leave_Table
from rest_framework import exceptions


import json
import base64

class RegisterUserView(generics.CreateAPIView):
    """Register a new user and return a token for the user"""

    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = serializer.get_token(user)
        serializer.validated_data["token"] = token
        return super().perform_create(serializer)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Get and update user profile"""

    serializer_class = UserProfileSeralizer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_object(self):
        return self.request.user
    

class registerEmployeeView(APIView):
    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = serializer.get_token(user)
        serializer.validated_data["token"] = token
        return super().perform_create(serializer)
    
    
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = Employee.objects.filter(email = email).first()
        
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credential')
        
        if user.password !=request.data['password']:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        
        access_token = create_access_tokken(user.id)
        refresh_token = create_refresh_tokken(user.id)
        location=user.location_id.address
         
        avatar_data = None
        if user.avatar:
            with open(user.avatar.path, 'rb') as avatar_file:
                # avatar_data = base64.b64encode(avatar_file.read()).decode('utf-8')
                avatar_path = str(user.avatar) if user.avatar else None
        print(type(user.avatar))
        resized_img=user.avatar
        from django.http import HttpResponse
        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'user_id':user.id,
            'email':user.email,
            'CNIC':user.CNIC,
            'name':user.name,
            'location':location,
            'token': access_token,
            'avatar': avatar_path,
            'joining_date':user.joining_date,
            
            'time_in':user.time_in,
            'time_out':user.time_out,
            'password':user.password,
            #'avatar':(user.avatar).encode("utf-8"),
        }

        # json_data = json.dumps(response, indent=2)

        # # Print or use the JSON data as needed
        # print(json_data)

        # response.data = response
        return response
        



class AttendanceListView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
class AttendanceCreateView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
class AttendanceUpdateView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceUpdateSerializer

    def update(self, request, *args, **kwargs):
        attendance_id = self.kwargs['attendance_id']
        attendance = Attendance.objects.get(attendance_id=attendance_id)
        serializer = AttendanceUpdateSerializer(instance=attendance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=204)
    

# Emp_Register new code

class Emp_Register_View(generics.CreateAPIView):
    """Register a new user and return a token for the user"""

    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = serializer.get_token(user)
        serializer.validated_data["token"] = token
        return super().perform_create(serializer)

# new listemployee

class employeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# updata EmployeeUpdateView
class EmployeeUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeUpdateSerializer

    def update(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        employee = Employee.objects.get(id=user_id)
        serializer = EmployeeUpdateSerializer(instance=employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=204)



    #new code
class Salary_tableListView(ListAPIView):
    queryset = Salary_table.objects.all()
    serializer_class = Salary_tableSerializer

class Salary_tableCreateView(CreateAPIView):
    queryset = Salary_table.objects.all()
    serializer_class = Salary_tableSerializer


class Salary_tableUpdateView(UpdateAPIView):
    queryset = Salary_table.objects.all()
    serializer_class = Salary_tableSerializer

    def update(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        attendance = Salary_table.objects.get(user_id=user_id)
        serializer = Salary_tableSerializer(instance=Salary_table, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=204)  
    


 #new code   Leave_table
class Leave_TableListView(ListAPIView):
    queryset = Leave_Table.objects.all()
    serializer_class = Leave_TableSerializer

class Leave_TableCreateView(CreateAPIView):
    queryset = Leave_Table.objects.all()
    serializer_class = Leave_TableSerializer
    

# update leave 


class Leave_TableUpdateView(UpdateAPIView):
    queryset = Leave_Table.objects.all()
    serializer_class = Leave_TableUpdateSerializer

    def update(self, request, *args, **kwargs):
        leave_id = self.kwargs['leave_id']
        Leave = Leave_Table.objects.get(leave_id=leave_id)
        serializer = Leave_TableUpdateSerializer(instance=Leave, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=204)
# class Leave_TableUpdateView(UpdateAPIView):
#     queryset = Leave_Table.objects.all()
#     serializer_class = Leave_TableUpdateSerializer

#     def update(self, request, *args, **kwargs):
#         leave_id = self.kwargs['leave_id']
#         leave_table = get_object_or_404(Leave_Table, leave_id=leave_id)

#         serializer = Leave_TableUpdateSerializer(instance=leave_table, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(status=204)