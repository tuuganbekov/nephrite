from django.urls import path
from products.views import ProductList, ProductsByCategory, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('by-category/<int:pk>/', ProductsByCategory.as_view(), name='by-category'),
] 