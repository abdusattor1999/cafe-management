from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "accounts"

router = DefaultRouter()
router.register("user", views.UserViewset, basename="users")

urlpatterns = [
    path("registration/", views.RegisterView.as_view(), name="register"),
    path('verification/', views.VerifyView.as_view(), name='verify'),
    path("authentication/", views.LoginView.as_view(), name="login"),
    path("users/", views.UserListView.as_view(), name="users_list"),
]+router.urls

