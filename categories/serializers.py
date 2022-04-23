from dataclasses import fields
from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    children = serializers.ListField(read_only=True)
    