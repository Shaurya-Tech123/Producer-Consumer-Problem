from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Command(BaseCommand):
    help = 'Create or fix the viewer user account'

    def handle(self, *args, **options):
        # Delete any existing viewer users first
        User.objects.filter(username='viewer').delete()
        self.stdout.write("Deleted any existing viewer users")
        
        # Create fresh viewer user
        viewer = User.objects.create_user(
            username='viewer',
            password='viewer12345',
            is_staff=False,
            is_active=True
        )
        self.stdout.write(f"Created viewer user: {viewer.username}")
        
        # Test authentication
        test_user = authenticate(username='viewer', password='viewer12345')
        if test_user:
            self.stdout.write(
                self.style.SUCCESS("Authentication test PASSED")
            )
            self.stdout.write("You can now login with:")
            self.stdout.write("  Username: viewer")
            self.stdout.write("  Password: viewer12345")
        else:
            self.stdout.write(
                self.style.ERROR("Authentication test FAILED")
            )
