from rest_framework.serializers import ModelSerializer

from site_images.models import Image


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
        