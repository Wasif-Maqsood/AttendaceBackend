from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Emp_Register_View, RegisterUserView, UserProfileView, employeeListView
from .views import LoginView,AttendanceCreateView,AttendanceListView,AttendanceUpdateView#, EmployeeListView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path('Emplogin/', LoginView.as_view(), name='login'),
    path('Emp_Register_View/',Emp_Register_View.as_view()),
    
       

    path('listemployee/', employeeListView.as_view()),
  
    
    path('markattendance/', AttendanceCreateView.as_view()),
    path('updateattendance/<int:attendance_id>', AttendanceUpdateView.as_view()),
    path('listattendance/', AttendanceListView.as_view()),
    
    #path('employees/', EmployeeListView.as_view(), name='employees'),


]
