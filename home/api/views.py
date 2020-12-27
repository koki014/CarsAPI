
from rest_framework.views import APIView
from rest_framework.response import Response
from home.api.serializers import CarSerializer, CarCreateSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from home.models import Car



class CarsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cars = Car.objects.filter(is_published=True)
        serilizer = CarSerializer(cars, many=True, context = {'request' : request})
        return Response(data=serilizer.data, status=HTTP_200_OK)


    def post(self, request, *args, **kwargs):
            recipe_data = request.data
            serializer = CarCreateSerializer(data=recipe_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)



