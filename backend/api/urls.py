from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('customers', views.SearchCustomerViewSet, basename='customer')
router.register('products', views.SearchProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('random/reviews', views.RandomReviewsListView.as_view(), name='list_random_reviews'),
    path('ml-models/list', views.MLModelListView.as_view(), name='list_ml-models'),
    path('ml-models/customers/count', views.getCustomersCount, name='ml-models-customers-count'),
]
