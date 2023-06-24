"""
Serializers for the positive things API.
"""
from rest_framework import serializers

from core.models import PositiveThings

class PositiveThingsSerializer(serializers.ModelSerializer):
    """Serializer for positive things."""
    class Meta:
        model = PositiveThings
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a positive thing."""
        positive_thing = PositiveThings.objects.create(**validated_data)
        return positive_thing
