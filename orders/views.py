from rest_framework import views, response, status
from django.core.mail import send_mail
from django.conf import settings

from orders.models import Order, Order_product
from orders.serializers import OrderSerializer
from products.models import Product


# Create your views here.
class GetOrdersApiView(views.APIView):

    def get(self, request, format=None):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class MakeOrderApiView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        order_data = request.data
        products = order_data.pop('products')
        order = Order.objects.create(**order_data, total_sum=0)
        total_sum = 0
        for item in products:
            product = Product.objects.get(id=item.get("product"))
            quantity = item.get("quantity")
            order_product = Order_product.objects.create(
                                                        product=product, 
                                                        order=order,
                                                        quantity=quantity
                                                    )
            if product.new_price:
                product_price = product.new_price
            else:
                product_price = product.old_price
            total_price = product_price * quantity
            order_product.total_price = total_price
            total_sum += total_price
            order_product.save()
            product.quantity -= quantity
            product.save()
        
        order.total_sum = total_sum
        order.save()
        
        # gmail notification
        # http_header = request.META
        send_mail(
            "Новый заказ",
            f"От: {order.full_name}\nПочта: {order.email}\nТелефон: {order.phone}\nАдрес: {order.address}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
        )
        return response.Response({"message": "Заказ принят."}, status=status.HTTP_200_OK)
