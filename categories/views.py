from rest_framework import views, response, status
from categories.models import Category
from categories.serializers import CategorySerializer


# Create your views here.
class CategoryList(views.APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all categories.
        """
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
