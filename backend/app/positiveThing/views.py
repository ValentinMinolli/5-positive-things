"""
Views for the positive things API.
"""
from drf_spectacular import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import(
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import PositiveThings

from positiveThing import serializers


class PositiveThingsViews(viewsets.ModelViewSet):
    """View for the manage positive things API."""
    serializer_class = serializers.PositiveThings
    queryset = PositiveThings.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve a list of positive things for the authenticated user."""
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user,
        ).order_by('-id').distinct()
    
    def perform_create(self, serializer):
        """Create a new positive thing."""
        serializer.save(user=self.request.user)
        
