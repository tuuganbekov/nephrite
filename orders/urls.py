from django.urls import path

from orders.views import MakeOrderApiView, GetOrdersApiView

app_name = 'orders'

urlpatterns = [
    path('', GetOrdersApiView.as_view()),
    path('make-order/', MakeOrderApiView.as_view()),
] 
