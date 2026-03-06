#---------------------------
# New Offer Details
#---------------------------
from django.urls import path
from .views import (
    NewOfferListCreateView,
    NewOfferDetailView,
)

urlpatterns = [
    path("", NewOfferListCreateView.as_view(), name="offer-list-create"),
    path("<int:pk>/", NewOfferDetailView.as_view(), name="offer-detail"),
]
#-----------------------
# New Target
#------------------------
from django.urls import path
from .views import (
    NewTargettingListCreateView,
    NewTargettingDetailView,
)

urlpatterns = [
    path("targetting/", NewTargettingListCreateView.as_view(), name="targetting-list-create"),
    path("targetting/<int:pk>/", NewTargettingDetailView.as_view(), name="targetting-detail"),
]
#-----------------------
# dashboard
#-----------------------
from django.urls import path
from .views import (
    DashboardListCreateView,
    DashboardDetailView,
)

urlpatterns = [
    path("dashboard/", DashboardListCreateView.as_view(), name="dashboard-list-create"),
    path("dashboard/<int:pk>/", DashboardDetailView.as_view(), name="dashboard-detail"),
]