from django.urls import path
from categories.views import CategoryList, CategoryDetailApiView


urlpatterns = [
    path('', CategoryList.as_view(), name='category-list'),
    path('<int:pk>/', CategoryDetailApiView.as_view(), name='category-detail'),
] 