#--------------------------
# New Agent 
#-------------------------
from django.urls import path
from .views import NewAgentListCreateView, NewAgentDetailView
urlpatterns = [
    path('', NewAgentListCreateView.as_view(), name='new-agent-list-create'),
    path('<int:pk>/', NewAgentDetailView.as_view(), name='new-agent-detail'),
]
#----------------------------
# Dashboard
#-----------------------------
from django.urls import path
from .views import DashboardListCreateView, DashboardDetailView
urlpatterns = [
    path('dashboard/', DashboardListCreateView.as_view(), name='dashboard-list-create'),
    path('dashboard/<int:pk>/', DashboardDetailView.as_view(), name='dashboard-detail'),
]
#---------------------------------
# all agent
#---------------------------------
from django.urls import path
from .views import AllAgentListCreateView, AllAgentDetailView

urlpatterns = [
    path('all-agent/', AllAgentListCreateView.as_view(), name='all-agent-list-create'),
    path('all-agent/<int:pk>/', AllAgentDetailView.as_view(), name='all-agent-detail'),
]
#------------------------------
# Edit Agent
#------------------------------
from django.urls import path
from .views import EditAgentListCreateView, EditAgentDetailView

urlpatterns = [
    path('edit-agent/', EditAgentListCreateView.as_view(), name='edit-agent-list-create'),
    path('edit-agent/<int:pk>/', EditAgentDetailView.as_view(), name='edit-agent-detail'),
]
#------------------------- 
# View agent
#-------------------------
from django.urls import path
from .views import ViewAgentListCreateView, ViewAgentDetailView

urlpatterns = [
    path('view-agent/', ViewAgentListCreateView.as_view(), name='view-agent-list'),
    path('view-agent/<int:pk>/', ViewAgentDetailView.as_view(), name='view-agent-detail'),
]
#-----------------------
# Remove Agent
#------------------------
from django.urls import path
from .views import RemoveAgentView

urlpatterns = [
    path('remove-agent/', RemoveAgentView.as_view(), name='remove-agent'),
]