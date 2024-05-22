from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterUserView, UserProfileView,Emp_Register_View
from .views import LoginView,registerEmployeeView,AttendanceCreateView,employeeListView,AttendanceListView,AttendanceUpdateView,Salary_tableListView,Leave_TableListView,Leave_TableUpdateView,Leave_TableCreateView,EmployeeUpdateView  #, EmployeeListView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path('Emplogin/', LoginView.as_view(), name='login'),
    path('empregister/', registerEmployeeView.as_view()),

    path('listemployee/', employeeListView.as_view()),
    
    path('markattendance/', AttendanceCreateView.as_view()),
    path('updateattendance/<int:attendance_id>', AttendanceUpdateView.as_view()),
    path('updateleave/<int:leave_id>', Leave_TableUpdateView.as_view()),
    path('listattendance/', AttendanceListView.as_view()),
    path('Emp_Register_View/',Emp_Register_View.as_view()),
    path('updateemployee/<int:user_id>', EmployeeUpdateView.as_view()),
    path('Salary_table/', Salary_tableListView.as_view()), 
    path('Leave/',Leave_TableCreateView.as_view()), 
    path('Leave_Table/',Leave_TableListView.as_view()),
    # path('Leave_Table_update/',Leave_TableUpdateView.as_view()), 
    
    #path('employees/', EmployeeListView.as_view(), name='employees'),
    
    #  path('update/<int:pk>/', Leave_TableUpdateView.as_view(), name='leave_table-update'),
]
