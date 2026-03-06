from rest_framework import serializers
from .models import Dashboard

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"
#------------------------
# Recent agents
#------------------------
from rest_framework import serializers
from .models import RecentAgent

class RecentAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentAgent
        fields = "__all__"
#---------------------------
# create Account
#---------------------------
from rest_framework import serializers
from .models import Create_Account
from django.contrib.auth.hashers import make_password


class CreateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Create_Account
        fields = "__all__"

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
#---------------------------
# Sign in
#--------------------------
from rest_framework import serializers
from .models import Sign_in
from django.contrib.auth.hashers import make_password


class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sign_in
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)