import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_demandflow.settings")
django.setup()

from django.contrib.auth.models import User
from hotel_queue.models import HotelSettings, StaffRole, StaffMember

# Create or update superuser with a guaranteed password
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin12345"
ADMIN_EMAIL = "admin@example.com"
admin_user, admin_created = User.objects.get_or_create(username=ADMIN_USERNAME, defaults={"email": ADMIN_EMAIL})
admin_user.is_staff = True
admin_user.is_superuser = True
admin_user.is_active = True
admin_user.set_password(ADMIN_PASSWORD)
admin_user.save()
if admin_created:
    print("Superuser created: admin / admin12345")
else:
    print("Superuser updated: password reset to admin12345")

# Ensure one HotelSettings row
HotelSettings.objects.get_or_create(id=1, defaults={"num_tables": 10, "num_rooms": 10})

# Seed roles
role_names = [
    "Waiter",
    "Cleaner",
    "Maintenance Staff",
    "Billing Staff",
    "Room Service Staff",
]
roles = {}
for name in role_names:
    role, _ = StaffRole.objects.get_or_create(name=name)
    roles[name] = role

# Seed staff
staff_seed = [
    ("Ramesh", "Waiter"),
    ("Sita", "Cleaner"),
    ("Karan", "Maintenance Staff"),
    ("Meera", "Billing Staff"),
    ("Ajay", "Room Service Staff"),
]
for staff_name, role_name in staff_seed:
    StaffMember.objects.get_or_create(name=staff_name, role=roles[role_name])

print("Seeding complete.")

# Create or update a viewer (non-staff) user with known password
VIEWER_USERNAME = "viewer"
VIEWER_PASSWORD = "viewer12345"
viewer, created = User.objects.get_or_create(username=VIEWER_USERNAME, defaults={"is_staff": False})
viewer.is_staff = False
viewer.is_active = True
viewer.set_password(VIEWER_PASSWORD)
viewer.save()
if created:
    print("Viewer user created: viewer / viewer12345")
else:
    print("Viewer user updated: password reset to viewer12345, ensured active & non-staff")


