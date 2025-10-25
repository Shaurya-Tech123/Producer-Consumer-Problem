from django.conf import settings
from django.db import models


class Demand(models.Model):
    DEMAND_TYPES = [
        ("Food", "Food"),
        ("Cleaning", "Cleaning"),
        ("Maintenance", "Maintenance"),
        ("Billing", "Billing"),
        ("Room Service", "Room Service"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    demand_type = models.CharField(max_length=32, choices=DEMAND_TYPES)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    expected_completion = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="demands_created", on_delete=models.CASCADE)
    fulfilled_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="demands_fulfilled", on_delete=models.SET_NULL, null=True, blank=True)
    # For Food demands only
    quantity = models.PositiveIntegerField(null=True, blank=True)
    room_or_table = models.CharField(max_length=32, null=True, blank=True)
    # No food-specific fields in the simplified version

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.demand_type} - {self.status}: {self.description[:30]}"


class HotelSettings(models.Model):
    num_tables = models.PositiveIntegerField(default=10)
    num_rooms = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"Settings (tables={self.num_tables}, rooms={self.num_rooms})"


class StaffRole(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class StaffMember(models.Model):
    name = models.CharField(max_length=64)
    role = models.ForeignKey(StaffRole, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return f"{self.name} ({self.role.name})"


# Link demand to assigned staff member (manual assignment)
Demand.add_to_class("assigned_to", models.ForeignKey(StaffMember, on_delete=models.SET_NULL, null=True, blank=True))


