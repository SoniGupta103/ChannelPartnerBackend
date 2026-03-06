#------------------------
# Dashboard
#------------------------
from django.urls import path
from .views import DashboardListCreateView, DashboardDetailView

urlpatterns = [
    path("", DashboardListCreateView.as_view(), name="dashboard-list-create"),
    path("<int:pk>/", DashboardDetailView.as_view(), name="dashboard-detail"),
]
#------------------------
# Add Tenant
#------------------------
from django.urls import path
from .views import TenantListCreateView, TenantDetailView

urlpatterns = [
    path("", TenantListCreateView.as_view(), name="tenant-list-create"),
    path("<int:pk>/", TenantDetailView.as_view(), name="tenant-detail"),
]
#----------------------------
# Show Tenant
#----------------------------
from django.urls import path
from .views import ShowTenantListCreateView, ShowTenantDetailView

urlpatterns = [
    path("", ShowTenantListCreateView.as_view(), name="show-tenant-list-create"),
    path("<int:pk>/", ShowTenantDetailView.as_view(), name="show-tenant-detail"),
]