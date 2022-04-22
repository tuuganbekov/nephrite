from django.urls import path

from promotions.views import PromotionsApiView

urlpatterns = [
    path('', PromotionsApiView.as_view())
]
