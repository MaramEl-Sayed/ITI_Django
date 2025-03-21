from django.contrib import admin
from django.urls import path, include

# Ensure this path is correct:
from ITI.views import login_view, register_view ,logout_view 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name="login"),
    path("logout/",logout_view,name="logout"),
    path("register/", register_view, name="register"),
    path("trainee/", include("trainee_app.urls")),
    path("course/", include("course_app.urls")),
]
