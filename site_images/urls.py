from django.urls import path

from site_images.views import ImagesApiView

urlpatterns = [
    path('images/', ImagesApiView.as_view())
]