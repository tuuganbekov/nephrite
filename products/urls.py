from django.urls import path
from products.views import ProductList, ProductsByCategory

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('by-category/<int:pk>/', ProductsByCategory.as_view(), name='by-category'),
] 