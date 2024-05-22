from .models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, UserProfileSeralizer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets

from .models import Attendance
from .serializers import AttendanceSerializer,AttendanceUpdateSerializer
# import ValidationError from rest_framework.exceptions
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import EmployeeSerializer
from .authentication import create_access_tokken, create_refresh_tokken
from .models import Employee,Location
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

    

# class employeeListView(ListAPIView):
#     def get(self,request):
#         return Response(request.data)

class employeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


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
        
        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'user_id':user.id,
            'email':user.email,
            'name':user.name,
            'token': access_token
        }

        #return response
        return (response)
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