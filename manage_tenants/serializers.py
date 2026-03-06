#------------------------
# Dashboard
#------------------------
from rest_framework import serializers
from .models import Dashboard
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"
#------------------------
# Add Tenant
#------------------------
from rest_framework import serializers
from .models import NewTenant


class NewTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTenant
        fields = "__all__"
#----------------------------
# Show Tenant
#----------------------------
from rest_framework import serializers
from .models import ShowTenant


class ShowTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTenant
        fields = "__all__"