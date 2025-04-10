from django.urls import path, include
from api import views
# from accounts import views as account_views
# from referrals import views as referrals_views
# from partners import views as partners_views
# from core import views as core_views
from rest_framework.routers import DefaultRouter
# from general import views as general_views
# from home import views as home_views

app_name = 'api'

router = DefaultRouter()
router.register('customers', views.SearchCustomerViewSet, basename='customer')
router.register('products', views.SearchProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    # path('icons-about/', views.IconAboutListView.as_view(), name='list_icons_about'),
]
