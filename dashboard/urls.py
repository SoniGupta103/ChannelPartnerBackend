# dashboard/urls.py
from django.urls import path
from .views import (
    DashboardListCreateView, DashboardDetailView,
    RecentAgentListCreateView, RecentAgentDetailView,
    CreateAccountListCreateView, CreateAccountDetailView,
    SignInListCreateView, SignInDetailView,
)

urlpatterns = [
    # Dashboard
    path('dashboard/', DashboardListCreateView.as_view(), name='dashboard-list-create'),
    path('dashboard/<int:pk>/', DashboardDetailView.as_view(), name='dashboard-detail'),

    # Recent Agents
    path('recent-agents/', RecentAgentListCreateView.as_view(), name='recent-agent-list-create'),
    path('recent-agents/<int:pk>/', RecentAgentDetailView.as_view(), name='recent-agent-detail'),

    # Accounts
    path('accounts/', CreateAccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', CreateAccountDetailView.as_view(), name='account-detail'),

    # Sign In
    path('sign-in/', SignInListCreateView.as_view(), name='sign-in-list-create'),
    path('sign-in/<int:pk>/', SignInDetailView.as_view(), name='sign-in-detail'),
]