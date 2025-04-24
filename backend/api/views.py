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
from api.models import Review
from api.models import MLModel
from api.models import CustomerFeaturesCurrent
from django.db.models import Q

from api.paginators import StandardResultsSetPagination
from api import serializers as api_serializers

import random
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework.decorators import action
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from api.services.machine_learning import get_customer_xdata
from api.services.machine_learning import normalize_customer_xdata
from api.services.machine_learning import load_ml_model
from api.services.machine_learning import get_predict_interpretation
from api.services.machine_learning import get_xdata_properties
from api.services.reports import churn_sales_report

from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)


class SearchCustomerViewSet(ModelViewSet):
    # serializer_class = api_serializers.CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = StandardResultsSetPagination
    def get_serializer_class(self):
        if self.request.method == 'GET' and 'pk' in self.kwargs:
            return api_serializers.CustomerDetailSerializer
        return api_serializers.CustomerSerializer

    def list(self, request, *args, **kwargs):
        
        threshold = request.GET.get('threshold', None)

        queryset = Customer.objects.all()
        if threshold:
            unique_ids = (CustomerFeaturesCurrent.objects
                .filter(pred_proba__gte=threshold)
                .values_list('customer_unique_id', flat=True)
                .distinct())
            queryset = queryset.filter(customer_unique_id__in=unique_ids)

        queryset = queryset.order_by('-orders_total')
        # queryset = queryset.filter(pred_proba__isnull=False).order_by('-pred_proba')
        page = self.paginate_queryset(queryset)
        serializer = api_serializers.CustomerSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)
    
    @action(methods=['get'], detail=True)
    def predict(self, request, pk=None, *args, **kwargs):
        сustomer = Customer.objects.get(pk=pk)
        xdata = get_customer_xdata(сustomer.customer_unique_id)
        mlmodels = MLModel.objects.filter(is_active=True).all()
        
        predicts = []
        for mlmodel in mlmodels:
            df_X = normalize_customer_xdata(mlmodel, xdata)
            mlmodel_worker = load_ml_model(mlmodel.model_file)
            proba = mlmodel_worker.predict_proba(df_X)[:, 1]
            interpretations = get_predict_interpretation(mlmodel_worker, df_X)
            predicts.append({
                'mlmodel': api_serializers.MLModelLightSerializer(mlmodel, many=False).data,
                'proba': proba,
                'interpretations': interpretations
            })
        x_items = df_X.to_dict('records')
        properties = get_xdata_properties(x_items[0]) if len(x_items) else []
        return Response({
            'properties': properties,
            'predicts': predicts
        }, status=HTTP_200_OK)


class SearchProductViewSet(ModelViewSet):
    serializer_class = api_serializers.ProductSerializer
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        page = self.paginate_queryset(queryset)
        serializer = api_serializers.ProductSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)


class RandomReviewsListView(ListAPIView):
    serializer_class = api_serializers.ReviewSerializer
    def get_queryset(self):
        sliсe_count = random.randint(0, 1000)
        return Review.objects.filter(message_ru__isnull=False)[sliсe_count:5 + sliсe_count]
        # return Review.objects.filter(message_ru__isnull=False, review_id='2c5e27fc-178b-de7a-c173-c9c62c31b070')


class MLModelListView(ListAPIView):
    serializer_class = api_serializers.MLModelSerializer
    queryset = MLModel.objects.all()


@api_view(('GET',))
@permission_classes((AllowAny,))
def getCustomersCount(request):

    threshold = request.GET.get('threshold', 0.5)
    # count = CustomerFeaturesCurrent.objects.filter(pred_proba__gte=threshold).count()
    unique_ids = (CustomerFeaturesCurrent.objects
              .filter(pred_proba__gte=threshold)
              .values_list('customer_unique_id', flat=True)
              .distinct())
    count = len(unique_ids)
    
    return Response({
        'count': count,
    }, status=HTTP_200_OK)



@api_view(('GET',))
@permission_classes((AllowAny,))
def churnSalesReport(request):
    report_type = request.GET.get('type', 'sales')
    selector_sign = '<' if report_type == 'churn' else '>='
    if report_type == 'sales':
        items = churn_sales_report(selector_sign)[-12:]
    elif report_type == 'churn':
        result = []
        items = churn_sales_report(selector_sign)

        # Первый элемент оставляем как есть
        first_item = {
            'timeline_month': items[0]['timeline_month'],
            'customer_count': items[0]['customer_count'],
            'count_diff': items[0]['customer_count']  # Для первого элемента разница = самому значению
        }
        result.append(first_item)
        for i in range(1, len(items)):
            # Вычисляем разницу с предыдущим значением
            difference = items[i]['customer_count'] - items[i-1]['customer_count']
            
            # Если разница отрицательная - ставим 0
            if difference < 0:
                difference = 0
            
            # Создаем новый элемент со всеми полями
            new_item = {
                'timeline_month': items[i]['timeline_month'],
                'customer_count': items[i]['customer_count'],
                'count_diff': difference
            }
            result.append(new_item)
        items = result[-14:-2]
    return Response(items, status=HTTP_200_OK)
