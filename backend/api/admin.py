from django.contrib import admin

from api.models import Customer
from api.models import Product
from api.models import Review
from api.models import MLModel
from api.models import CustomerFeaturesCurrent


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'customer_unique_id',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_id',
        'product_category_name',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'review_id',
        'order_id',
        'score',
        'message_ru',
    ]


@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'model_file',
        'precision_true',
        'recall_true',
        'f1_true',
        'precision_false',
    ]


@admin.register(CustomerFeaturesCurrent)
class CustomerFeaturesCurrentAdmin(admin.ModelAdmin):
    list_display = [
        'order_id',
        'customer_unique_id',
        'timeline_date',
        'pred_proba'
    ]

