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


class PositiveThingsViewSet(viewsets.ModelViewSet):
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

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'assigned_only',
                OpenApiTypes.INT, enum=[0, 1],
                description='Filter by dates assigned to positive things.',
            )
        ]
    )
)

class BasePositiveThingsAttrViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Base viewset for positive things attributes."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only'))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(positive_things__isnull = False)
        
        return queryset.filter(
            user=self.request.user
        ).order_by('-title').distinct()
