#-----------------------------
# add record
#-----------------------------
from django.urls import path
from .views import (
    RecoveryRecordListCreateView,
    RecoveryRecordDetailView,
)

urlpatterns = [
    path("", RecoveryRecordListCreateView.as_view(), name="recovery-record-list-create"),
    path("<int:pk>/", RecoveryRecordDetailView.as_view(), name="recovery-record-detail"),
]
#-------------------------
# Dashboard
#-------------------------
from django.urls import path
from .views import (
    DashboardListCreateView,
    DashboardDetailView,
)

urlpatterns = [
    path("dashboard/", DashboardListCreateView.as_view(), name="dashboard-list-create"),
    path("dashboard/<int:pk>/", DashboardDetailView.as_view(), name="dashboard-detail"),
]
#---------------------------
# search
#---------------------------
from django.urls import path
from .views import (
    RecoverySearchListCreateView,
    RecoverySearchDetailView,
)
urlpatterns = [
    path("recovery-search/", RecoverySearchListCreateView.as_view(), name="recovery-search-list-create"),
    path("recovery-search/<int:pk>/", RecoverySearchDetailView.as_view(), name="recovery-search-detail"),
]
#----------------------------------
# Recovery payment main edit
#-----------------------------------
from django.urls import path
from .views import (
    EditRecoveryListCreateView,
    EditRecoveryDetailView,
)

urlpatterns = [
    path("edit-recovery/", EditRecoveryListCreateView.as_view(), name="edit-recovery-list-create"),
    path("edit-recovery/<int:pk>/", EditRecoveryDetailView.as_view(), name="edit-recovery-detail"),
]