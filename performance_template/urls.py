#-------------------------
# Dashboard
#-------------------------
from django.urls import path
from .views import DashboardListCreateView, DashboardDetailView

urlpatterns = [
    path('dashboard/', DashboardListCreateView.as_view(), name='dashboard-list'),
    path('dashboard/<int:pk>/', DashboardDetailView.as_view(), name='dashboard-detail'),
]
#---------------------
# New Template
#----------------------
from django.urls import path
from .views import TemplateListCreateView, TemplateDetailView

urlpatterns = [
    path("", TemplateListCreateView.as_view(), name="template-list-create"),
    path("<int:pk>/", TemplateDetailView.as_view(), name="template-detail"),
]