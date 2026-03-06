# dashboard/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Dashboard, RecentAgent, Create_Account, Sign_in
from .serializers import (
    DashboardSerializer, RecentAgentSerializer,
    CreateAccountSerializer, SignInSerializer,
)

class DashboardListCreateView(ListCreateAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

class DashboardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

class RecentAgentListCreateView(ListCreateAPIView):
    queryset = RecentAgent.objects.all()
    serializer_class = RecentAgentSerializer

class RecentAgentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RecentAgent.objects.all()
    serializer_class = RecentAgentSerializer

class CreateAccountListCreateView(ListCreateAPIView):
    queryset = Create_Account.objects.all()
    serializer_class = CreateAccountSerializer

class CreateAccountDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Create_Account.objects.all()
    serializer_class = CreateAccountSerializer

class SignInListCreateView(ListCreateAPIView):
    queryset = Sign_in.objects.all()
    serializer_class = SignInSerializer

class SignInDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sign_in.objects.all()
    serializer_class = SignInSerializer