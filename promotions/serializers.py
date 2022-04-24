from rest_framework.serializers import ModelSerializer

from promotions.models import Promotion
from products.serializers import ProductSerializer


class PromotionSerializer(ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Promotion
        fields = '__all__'
