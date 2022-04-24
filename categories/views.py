from email.policy import default
from rest_framework import views, response, status
from categories.models import Category
from categories.serializers import CategorySerializer
from django.db.models import F, Q, OuterRef, When, Case, Exists
from django.contrib.postgres.expressions import ArraySubquery
from django.contrib.postgres.aggregates import ArrayAgg, JSONBAgg



# Create your views here.
class CategoryList(views.APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all categories.
        """
        queryset = Category.objects.filter(sub_category=None)
        
        data = []
        for item in queryset:
            data.append({
                'id': item.id,
                'title': item.title,
                'children': CategorySerializer(item.parent.all(), many=True).data
            })
        serializer = CategorySerializer(data, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
