from rest_framework.views import APIView
from rest_framework import response, status

from site_images.models import Image
from site_images.serializers import ImageSerializer


class ImagesApiView(APIView):

    def get(self, request, format=None):
        # query params image type id
        image_type = request.query_params.get('type')
        try:
            image = Image.objects.get(image_type=image_type)
            serializer = ImageSerializer(image)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except Image.DoesNotExist:
            return response.Response({"error_message": "Image does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
