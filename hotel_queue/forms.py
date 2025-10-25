from django import forms
from .models import Demand, HotelSettings, StaffRole, StaffMember


FOOD_CHOICES = [
    ("Pizza", "Pizza"),
    ("Burger", "Burger"),
    ("Sandwich", "Sandwich"),
    ("Pasta", "Pasta"),
    ("Coffee", "Coffee"),
    ("Tea", "Tea"),
    ("Juice", "Juice"),
    ("Rice Plate", "Rice Plate"),
    ("Salad", "Salad"),
]


class DemandForm(forms.ModelForm):
    food_item = forms.ChoiceField(choices=[("", "Select food item...")] + FOOD_CHOICES, required=False, widget=forms.Select(attrs={"class": "form-select", "id": "id_food_item"}))
    quantity = forms.IntegerField(required=False, min_value=1, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Quantity", "id": "id_quantity"}))
    room_or_table = forms.ChoiceField(required=False, choices=[("", "Select Room/Table...")], widget=forms.Select(attrs={"class": "form-select", "id": "id_room_or_table"}), label="Location")
    assigned_to = forms.ModelChoiceField(required=False, queryset=StaffMember.objects.all(), widget=forms.Select(attrs={"class": "form-select", "id": "id_assigned_to"}), label="Assigned To")
    expected_completion = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}))

    class Meta:
        model = Demand
        fields = ["demand_type", "description", "expected_completion", "quantity", "room_or_table", "assigned_to"]
        widgets = {
            "demand_type": forms.Select(attrs={"class": "form-select", "id": "id_demand_type"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Short description", "id": "id_description"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Description will be auto-filled for Food, so don't require it at field level
        self.fields["description"].required = False
        
        # Populate room/table choices from settings - merged into a single dropdown
        settings_qs = HotelSettings.objects.all()
        num_tables = settings_qs.first().num_tables if settings_qs.exists() else 10
        num_rooms = settings_qs.first().num_rooms if settings_qs.exists() else 10
        
        # Create a combined list of tables and rooms
        table_choices = [(f"Table {i}", f"Table {i}") for i in range(1, num_tables + 1)]
        room_choices = [(f"Room {100+i}", f"Room {100+i}") for i in range(1, num_rooms + 1)]
        combined_choices = [("", "Select Table or Room...")] + table_choices + room_choices
        
        # Set the choices for the room_or_table field
        self.fields["room_or_table"].choices = combined_choices
        
        # Update the placeholder text
        self.fields["room_or_table"].widget.attrs['placeholder'] = "Select Table or Room"
            
        # Populate assigned_to with only available staff members (not assigned to pending/in-progress demands)
        busy_staff_ids = Demand.objects.filter(status__in=["Pending", "In Progress"]).values_list('assigned_to_id', flat=True)
        available_staff = StaffMember.objects.select_related("role").exclude(id__in=busy_staff_ids)
        self.fields["assigned_to"].queryset = available_staff
        self.fields["assigned_to"].widget.attrs['placeholder'] = "Assign to Staff Member"

    def clean(self):
        cleaned = super().clean()
        demand_type = cleaned.get("demand_type")
        food_item = self.cleaned_data.get("food_item")
        description = cleaned.get("description")
        quantity = cleaned.get("quantity")
        room_or_table = cleaned.get("room_or_table")
        assigned_to = cleaned.get("assigned_to")
        if demand_type == "Food":
            if not food_item:
                self.add_error("food_item", "Please choose a food item.")
            if not quantity:
                quantity = 1
                cleaned["quantity"] = quantity
            if not room_or_table:
                self.add_error("room_or_table", "Please enter room/table number.")
            if food_item:
                cleaned["description"] = f"{food_item} (x{quantity})"
        else:
            if not description:
                self.add_error("description", "Please enter a short description.")
            if not room_or_table:
                self.add_error("room_or_table", "Please enter room/table number.")
        # Optional: filter assigned_to by role based on demand type
        role_map = {
            "Food": "Waiter",
            "Cleaning": "Cleaner",
            "Maintenance": "Maintenance Staff",
            "Billing": "Billing Staff",
            "Room Service": "Room Service Staff",
        }
        role_name = role_map.get(demand_type)
        if role_name:
            try:
                role = StaffRole.objects.get(name=role_name)
                self.fields["assigned_to"].queryset = StaffMember.objects.filter(role=role)
                if assigned_to and assigned_to.role != role:
                    self.add_error("assigned_to", f"Please choose a staff member with role {role_name}.")
            except StaffRole.DoesNotExist:
                pass
        return cleaned


