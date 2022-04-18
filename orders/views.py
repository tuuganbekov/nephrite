from rest_framework import views, response, status

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
        order = Order.objects.create(**order_data)
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
        order.total_sum = total_sum
        order.save()
        return response.Response({"message": "Successfully created."}, status=status.HTTP_200_OK)
