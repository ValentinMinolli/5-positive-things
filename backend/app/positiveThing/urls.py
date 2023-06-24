"""
URL mapping for the positive things app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from positiveThing import views

router = DefaultRouter()
router.register('positive things', views.PositiveThingsViewSet)
