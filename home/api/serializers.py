
from rest_framework import serializers
from django.db.models import fields
from home.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'model',
            'title',
            'fuel',
            'is_new',
            'image',
            'image_url',
        )

class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'model',
            'title',
            'fuel',
            'is_new',
            'image',
            'image_url',
        )

        