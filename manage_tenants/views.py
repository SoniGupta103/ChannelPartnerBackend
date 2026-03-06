#------------------------
# Dashboard
#------------------------
from rest_framework import generics
from .models import Dashboard
from .serializers import DashboardSerializer


class DashboardListCreateView(generics.ListCreateAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer


class DashboardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
#------------------------
# Add Tenant
#------------------------
from rest_framework import generics
from .models import NewTenant
from .serializers import NewTenantSerializer


class TenantListCreateView(generics.ListCreateAPIView):
    queryset = NewTenant.objects.all()
    serializer_class = NewTenantSerializer


class TenantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewTenant.objects.all()
    serializer_class = NewTenantSerializer
#----------------------------
# Show Tenant
#----------------------------
from rest_framework import generics
from .models import ShowTenant
from .serializers import ShowTenantSerializer


class ShowTenantListCreateView(generics.ListCreateAPIView):
    queryset = ShowTenant.objects.all()
    serializer_class = ShowTenantSerializer


class ShowTenantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShowTenant.objects.all()
    serializer_class = ShowTenantSerializer