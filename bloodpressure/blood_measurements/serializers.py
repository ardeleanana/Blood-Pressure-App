from django.db import models
from rest_framework import serializers
from .models import Measurements



from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser
from .models import GENDER_SELECTION


class CustomRegisterSerializer(RegisterSerializer):
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    phone_number = serializers.CharField(max_length=30)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.height = self.data.get('height')
        user.weight = self.data.get('weight')
        user.age = self.data.get('age')
        user.save()
        return user



class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'age',
            'gender',
            'weight',
            'height'

        )
        read_only_fields = ('pk', 'email', 'age','weight','height')



class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['id', 'systolic', 'diastolic', 'pulse','measurement_date']