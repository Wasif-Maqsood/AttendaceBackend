from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import EmailValidator
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Attendance

from .models import Employee


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


class EmployeeSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    email = serializers.EmailField(
        validators=[EmailValidator(), UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = Employee
        fields = ["name", "email","password","token","location_id","id"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
            
        }
    
    def get_token(self, user):
        token = RefreshToken.for_user(user)
        data = {"refresh": str(token), "access": str(token.access_token)}
        return data 

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['attendance_id','user_id', 'time_in', 'time_out']    
    def update(self, instance, validated_data):
        instance.time_out = validated_data.get("time_out", instance.time_out)
        instance.save()
        return instance   
class AttendanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['attendance_id','time_out']