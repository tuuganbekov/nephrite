from rest_framework.views import APIView
from rest_framework import response, status

from promotions.models import Promotion
from promotions.serializers import PromotionSerializer

class PromotionsApiView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Promotion.objects.filter(is_active=True)
        serializer = PromotionSerializer(queryset, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)
        