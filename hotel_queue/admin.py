from django.contrib import admin
from .models import Demand, HotelSettings, StaffRole, StaffMember


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ("id", "demand_type", "status", "created_at", "expected_completion", "completed_at", "room_or_table", "quantity", "assigned_to", "created_by", "fulfilled_by")
    list_filter = ("demand_type", "status", "created_at", "assigned_to")
    search_fields = ("description", "room_or_table", "created_by__username", "fulfilled_by__username", "assigned_to__name")
    ordering = ("-created_at",)


@admin.register(HotelSettings)
class HotelSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "num_tables", "num_rooms")


@admin.register(StaffRole)
class StaffRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role")
    list_filter = ("role",)
    search_fields = ("name", "role__name")


