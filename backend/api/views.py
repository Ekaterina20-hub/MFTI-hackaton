from datetime import timedelta
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import transaction
from django.db.models import Q
from django.db.models.aggregates import Count
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet, ViewSet
from api.models import Customer
from api.models import Product
from django.db.models import Q

from api.paginators import StandardResultsSetPagination
from api import serializers as api_serializers

import random
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)


class SearchCustomerViewSet(ModelViewSet):
    serializer_class = api_serializers.CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = Customer.objects.all()

        # get_service_id = request.GET.get('get_service', None)
        
        # if profile_id:
        #     profile = Profile.objects.get(id = profile_id)
        #     queryset = queryset.filter(user__profile = profile)

        page = self.paginate_queryset(queryset)
        serializer = api_serializers.CustomerSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)


class SearchProductViewSet(ModelViewSet):
    serializer_class = api_serializers.ProductSerializer
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        page = self.paginate_queryset(queryset)
        serializer = api_serializers.ProductSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)
