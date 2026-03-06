#------------------------
# Dashboard
#------------------------
from django.contrib import admin
from .models import Dashboard

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = (
        'total_agents',
        'Active_Agents',
        'Total_payouts',
        'lead_generated',
        'payouts_this_month',
        'pending_approvals',
        'offers_active',
        'Avg_Conversion_Rate',
        'date',
        'created_at'
    )
#------------------------
# Recent agents
#------------------------
from django.contrib import admin
from .models import RecentAgent

@admin.register(RecentAgent)
class RecentAgentAdmin(admin.ModelAdmin):
    list_display = ('agent_id', 'name', 'agent_type', 'payout', 'status', 'created_at')
    list_filter = ('status', 'agent_type')
    search_fields = ('agent_id', 'name')
#---------------------------
# create Account
#---------------------------
from django.contrib import admin
from .models import Create_Account


@admin.register(Create_Account)
class CreateAccountAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'full_name',
        'email',
        'phone',
        'role',
        'agree_terms',
        'create_account',
        'sign_in',
        'created_at',
    )

    list_filter = (
        'role',
        'agree_terms',
        'create_account',
        'sign_in',
        'created_at',
    )

    search_fields = (
        'user__username',
        'full_name',
        'email',
        'phone',
    )

    ordering = ('-created_at',)

    list_per_page = 20
#---------------------------
# Sign in
#--------------------------
from django.contrib import admin
from .models import Sign_in


@admin.register(Sign_in)
class SignInAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'rememeber_me',
        'sign_in',
        'create_account',
    )

    list_filter = (
        'rememeber_me',
        'sign_in',
        'create_account',
    )

    search_fields = (
        'email',
    )

    list_per_page = 20