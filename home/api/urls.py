from django.urls import path

from home.api.views import CarsAPIView

urlpatterns = [
    path('cars', CarsAPIView.as_view(), name='cars'),
]
