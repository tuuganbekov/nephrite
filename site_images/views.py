from rest_framework.views import APIView
from rest_framework import response, status

from site_images.models import Image


class ImagesApiView(APIView):

    def get(self, request, format=None):
        params = request.query_params
        return response.Response(status=status.HTTP_200_OK)
