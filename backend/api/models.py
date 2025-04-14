from django.db import models


class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customer_unique_id = models.UUIDField()
    state_code = models.CharField(max_length=250)
    city_id = models.IntegerField()
    orders_total = models.IntegerField()
    last_activity = models.DateField()
    avg_delivery_distance_km = models.FloatField()
    min_delivery_distance_km = models.FloatField()
    max_delivery_distance_km = models.FloatField()
    avg_expected_delivery_days = models.FloatField()
    avg_actual_delivery_days = models.FloatField()
    avg_delay = models.FloatField()
    avg_delay_factor = models.FloatField()
    avg_delivery_speed = models.FloatField()
    avg_delivery_cost = models.FloatField()
    avg_order_cost = models.FloatField()
    cancelled_ratio = models.FloatField()
    free_delivery_ratio = models.FloatField()
    sale_orders_ratio = models.FloatField()
    home_seller_ratio = models.FloatField()
    favorite_seller_state_code = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        db_table = 'analysis_geo_customers'
        managed = False


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True)
    product_category_name = models.CharField(max_length=250)
    product_name_lenght = models.IntegerField()
    product_description_lenght = models.IntegerField()
    product_photos_qty = models.IntegerField()
    product_weight_g = models.IntegerField()
    product_length_cm = models.IntegerField()
    product_height_cm = models.IntegerField()
    product_width_cm = models.IntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'products'
        managed = False


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True)
    order_id = models.UUIDField()
    score = models.IntegerField()
    message = models.CharField()
    message_ru = models.CharField()
    creation_date = models.DateField()
    q1 = models.BooleanField()
    q2 = models.IntegerField()
    q3 = models.BooleanField()
    q4 = models.BooleanField()
    q5 = models.BooleanField()
    q6 = models.IntegerField()
    q7 = models.BooleanField()
    q8 = models.BooleanField()
    q9 = models.IntegerField()
    q10 = models.BooleanField()
    q11 = models.BooleanField()
    customer_unique_id = models.UUIDField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'analysis_nlp_reviews'
        managed = False
