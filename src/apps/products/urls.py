from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("product", views.ProductViewset, basename="product")
router.register("category", views.CategoryViewset, basename="category")

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="products_list"),
    path("categories/", views.CategoryListView.as_view(), name="categories_list"),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/<int:pk>/', views.CartView.as_view(), name='cart-item'),
] + router.urls

