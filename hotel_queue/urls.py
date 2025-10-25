from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_demand, name="add_demand"),
    path("<int:pk>/in-progress/", views.mark_in_progress, name="mark_in_progress"),
    path("<int:pk>/complete/", views.mark_completed, name="mark_completed"),
    path("completed/", views.completed_list, name="completed_list"),
    path("completed/export/", views.export_completed_to_excel, name="export_completed"),
    path("completed/clear/", views.clear_completed_tasks, name="clear_completed"),
    path("settings/", views.settings_page, name="settings_page"),
    # Authentication routes
    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # TEMP: debug credential reset
    path("debug/reset-viewer/", views.reset_viewer_credentials, name="reset_viewer_credentials"),
    path("debug/whoami/", views.debug_whoami, name="debug_whoami"),
    path("debug/check-viewer/", views.debug_check_viewer, name="debug_check_viewer"),
]


