from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import EmailValidator
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Attendance,Salary_table,Leave_Table
from math import sqrt
from .models import Employee
from rest_framework.exceptions import ValidationError
from decimal import Decimal
logger = __import__("logging").getLogger(__name__)


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    email = serializers.EmailField(
        validators=[EmailValidator(), UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ["name", "email", "password", "token"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
            
        }

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        data = {"refresh": str(token), "access": str(token.access_token)}
        return data


class UserProfileSeralizer(serializers.ModelSerializer):
    """Use this serializer to get the user profile"""

    class Meta:
        model = User
        fields = ["id", "name", "email", "avatar"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.save()
        return instance




# new code

class EmployeeSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    email = serializers.EmailField(
        validators=[EmailValidator(), UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = Employee
        fields = ["avatar","name", "email","CNIC","phone","password","joining_date","designation","token","location_id","time_in", "time_out","id"]
        extra_kwargs = {
            "password": {"write_only": False, "min_length": 8},
            
        }
    
    def get_token(self, user):

        token = RefreshToken.for_user(user)
        data = {"refresh": str(token), "access": str(token.access_token)}
        if user.avatar:
            return user.avatar.url
        return data 
    
        if obj.avatar:
            return obj.avatar.url
        return None

# //////////////Update Employee///////////////////
from rest_framework import serializers

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["avatar", "name", "email", "CNIC", "phone", "password", "joining_date", "designation",  "location_id", "time_in", "time_out", "id"]

    name = serializers.CharField(allow_blank=True, required=False)
    avatar = serializers.ImageField(required=False)
    email = serializers.EmailField(required=False)
    CNIC = serializers.CharField(required=False)
    phone = serializers.CharField( required=False)
    password = serializers.CharField( required=False)
    joining_date = serializers.DateTimeField(required=False)
    designation = serializers.CharField( required=False)
      # Use ImageField for avatar
    # Add similar fields for other attributes you want to update

    def update(self, instance, validated_data):
        # Check if 'name' is provided in the validated_data and not set to None or blank
        if 'name' in validated_data and validated_data['name'] is not None and validated_data['name'] != '':
            new_name = validated_data['name']

            # Only update 'name' if it's different from the current value
            if instance.name != new_name:
                instance.name = new_name

        # Check if 'avatar' is provided in the validated_data and not set to None
        if 'avatar' in validated_data and validated_data['avatar'] is not None:
            new_avatar = validated_data['avatar']

            # Only update 'avatar' if it's different from the current value
            if instance.avatar != new_avatar:
                instance.avatar = new_avatar

        # Check if 'avatar' is provided in the validated_data and not set to None
        if 'email' in validated_data and validated_data['email'] is not None:
            new_email = validated_data['email']

            # Only update 'avatar' if it's different from the current value
            if instance.email != new_email:
                instance.email = new_email 

        # Check if 'avatar' is provided in the validated_data and not set to None
        if 'CNIC' in validated_data and validated_data['CNIC'] is not None:
            new_CNIC = validated_data['CNIC']

            # Only update 'avatar' if it's different from the current value
            if instance.CNIC != new_CNIC:
                instance.CNIC = new_CNIC         

        # Check if 'avatar' is provided in the validated_data and not set to None
        if 'phone' in validated_data and validated_data['phone'] is not None:
            new_phone = validated_data['phone']

            # Only update 'avatar' if it's different from the current value
            if instance.phone != new_phone:
                instance.phone = new_phone 

        # Check if 'avatar' is provided in the validated_data and not set to None
        if 'password' in validated_data and validated_data['password'] is not None:
            new_password = validated_data['password']

            # Only update 'avatar' if it's different from the current value
            if instance.password != new_password:
                instance.password = new_password  

        # Check if 'avatar' is provided in the validated_data and not set to None
        if 'joining_date' in validated_data and validated_data['joining_date'] is not None:
            new_joining_date = validated_data['joining_date']

            # Only update 'avatar' if it's different from the current value
            if instance.joining_date != new_joining_date:
                instance.joining_date = new_joining_date  

        # Check if 'designation' is provided in the validated_data and not set to None
        if 'designation' in validated_data and validated_data['designation'] is not None:
            new_designation = validated_data['designation']

         # Only update 'designation' if it's different from the current value
            if instance.designation != new_designation:
                instance.designation = new_designation                       


        # Update other fields (e.g., 'email', 'CNIC', 'phone', 'password', etc.)
        instance.email = validated_data.get("email", instance.email)
        instance.CNIC = validated_data.get("CNIC", instance.CNIC)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.password = validated_data.get("password", instance.password)
        instance.joining_date = validated_data.get("joining_date", instance.joining_date)
        instance.designation = validated_data.get("designation", instance.designation)
        # instance.token = validated_data.get("token", instance.token)
        instance.location_id = validated_data.get("location_id", instance.location_id)
        instance.time_in = validated_data.get("time_in", instance.time_in)
        instance.time_out = validated_data.get("time_out", instance.time_out)
        instance.id = validated_data.get("id", instance.id)

        instance.save()
        return instance








# class EmployeeSerializer(serializers.ModelSerializer):
#     token = serializers.SerializerMethodField()
#     email = serializers.EmailField(
#         validators=[EmailValidator(), UniqueValidator(queryset=User.objects.all())]
#     )
#     class Meta:
#         model = Employee
#         fields = ["id", "name", "email", "avatar","password"]
#         extra_kwargs = {
#             "password": {"write_only": True, "min_length": 8},
            
#         }
    
#     def get_token(self, user):
#         token = RefreshToken.for_user(user)
#         data = {"refresh": str(token), "access": str(token.access_token)}
#         return data 

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from math import sqrt

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['attendance_id', 'user_id', 'time_in', 'time_out','longitude','latitude']

    longitude = serializers.DecimalField(max_digits=39, decimal_places=36, write_only=True)
    latitude = serializers.DecimalField(max_digits=39, decimal_places=36, write_only=True)

    def create(self, validated_data):
        # Extract the `longitude` and `latitude` fields from validated data
        longitude = validated_data.pop('longitude', None)
        latitude = validated_data.pop('latitude', None)

        # Calculate the Euclidean distance
        target_latitude = Decimal('31.529319725960054')
        target_longitude = Decimal('74.34689634627284')
        distance = sqrt((latitude - target_latitude) ** 2 + (longitude - target_longitude) ** 2)

        if distance >0.0004:
            raise ValidationError("Distance is greater than 0.05")

        # Create and save the instance without `longitude` and `latitude`
        instance = Attendance.objects.create(**validated_data)

        return instance
class AttendanceUpdateSerializer(serializers.ModelSerializer):
    longitude = serializers.DecimalField(max_digits=39, decimal_places=36, write_only=True)
    latitude = serializers.DecimalField(max_digits=39, decimal_places=36, write_only=True)

    class Meta:
        model = Attendance
        fields = ['attendance_id', 'time_out', 'longitude', 'latitude']

    def update(self, instance, validated_data):
        # Update time_out
        instance.time_out = validated_data.get("time_out", instance.time_out)
        
        # Extract the `longitude` and `latitude` fields from validated data
        longitude = validated_data.get('longitude')
        latitude = validated_data.get('latitude')

        if longitude is not None and latitude is not None:
            # Calculate the Euclidean distance
            target_latitude = Decimal('31.529319725960054')
            target_longitude = Decimal('74.34689634627284')
            distance = sqrt((latitude - target_latitude) ** 2 + (longitude - target_longitude) ** 2)

            if distance <0.0005:
                instance.longitude = longitude
                instance.latitude = latitude
                instance.save()
            else:
                raise ValidationError(distance)

        return instance
    


# new code for salary
class Salary_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary_table
        fields = ["user_id","salary","date"]
    def update(self, instance, validated_data):
        instance.salary = validated_data.get("salary", instance.salary)
        instance.save()
        return instance             

class Salary_tableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary_table
        fields = ['user_id','salary','date']  




# Leave_Table
# class Leave_TableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Leave_Table
#         fields = ["user_id","date","leave_id","leave_reason","status"]
#     def update(self, instance, validated_data):
#         instance.salary = validated_data.get("Leave_Table", instance.salary)
#         instance.save()
#         return instance             
          


# /////////////leave  table view/////////////////
class Leave_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave_Table
        fields = ['leave_id', 'leave_reason', 'status', 'date','user_id']

# class Leave_TableUpdateSerializer(serializers.ModelSerializer):
#     leave_reason = serializers.CharField(max_length=100)
#     status = serializers.CharField(max_length=50)

#     class Meta:
#         model = Leave_Table
#         fields = ['leave_id', 'leave_reason', 'status', 'date']
      

# //////////////leave update//////////////
class Leave_TableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave_Table
        fields = ['leave_id', 'leave_reason', 'status', 'date', 'user_id']

    status = serializers.CharField(allow_blank=True, required=False)
    leave_reason = serializers.CharField(allow_blank=True, required=False)

    def update(self, instance, validated_data):
        # Check if 'status' is provided in the validated_data and not set to None or blank
        if 'status' in validated_data and validated_data['status'] is not None and validated_data['status'] != '':
            new_status = validated_data['status']

            # Only update 'status' if it's different from the current value
            if instance.status != new_status:
                instance.status = new_status

        # Check if 'leave_reason' is provided in the validated_data and not set to None or blank
        if 'leave_reason' in validated_data and validated_data['leave_reason'] is not None and validated_data['leave_reason'] != '':
            new_leave_reason = validated_data['leave_reason']

            # Only update 'leave_reason' if it's different from the current value
            if instance.leave_reason != new_leave_reason:
                instance.leave_reason = new_leave_reason

        # Update other fields (e.g., 'date', 'user_id') regardless of 'status' and 'leave_reason'
        instance.date = validated_data.get("date", instance.date)
        instance.user_id = validated_data.get("user_id", instance.user_id)

        instance.save()
        return instance







