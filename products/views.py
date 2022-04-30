from rest_framework import views, response, status
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
class ProductList(views.APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all products.
        """
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetail(views.APIView):
    def get(self, request, pk, format=None):
        """
        Return detail of the product
        """
        try:
            queryset = Product.objects.get(id=pk)
            serializer = ProductSerializer(queryset)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return response.Response({"message": "Product not found"})


class ProductsByCategory(views.APIView):
    
    def get(self, request, pk, format=None):
        """
        Return a list of all products.
        """
        queryset = Product.objects.filter(category=pk)
        serializer = ProductSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
