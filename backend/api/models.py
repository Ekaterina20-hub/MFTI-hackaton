import json
from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    # pred_proba = models.FloatField()

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        db_table = 'analysis_geo_customers'
        managed = False


class Product(models.Model):
    # product_id = models.UUIDField(primary_key=True)
    product_id = models.CharField(primary_key=True)
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


class MLModel(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Рабочее название модели",
        help_text="Человекочитаемое название модели",
        null=False,
        blank=False
    )
    model_file = models.CharField(
        max_length=255,
        verbose_name="Название файла модели",
        help_text="Имя файла с сохраненной моделью (например, model.cbm)",
        null=False,
        blank=False
    )
    # Метаданные для обработки данных
    feature_columns = ArrayField(
        models.CharField(max_length=100),
        verbose_name="Колонки признаков модели",
        help_text="Список колонок, которые использовались при обучении",
        default=list,
        blank=True
    )
    mean_values_json = models.JSONField(
        verbose_name="Средние значения для заполнения NA",
        help_text="JSON с средними/медианными значениями для заполнения пропусков",
        default=dict,
        blank=True
    )
    metrics_offset_json = models.JSONField(
        verbose_name="Смещение между recall и precision",
        help_text="JSON с коэффициентами для балансировки recall/precision",
        default=dict,
        blank=True
    )
    # Дополнительные метаданные
    precision_true = models.IntegerField(verbose_name="Precision - да")
    recall_true = models.IntegerField(verbose_name="Recall - да")
    f1_true = models.IntegerField(verbose_name="F1 - да")
    precision_false = models.IntegerField(verbose_name="Precision - нет")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "ML Модель"
        verbose_name_plural = "ML Модели"
        ordering = ['-created_at']
        db_table = 'api_mlmodel'
    
    def __str__(self):
        return f"{self.name} ({self.model_file})"
    
    def get_mean_values(self):
        """Возвращает средние значения как словарь"""
        try:
            return json.loads(self.mean_values_json)
        except (TypeError, json.JSONDecodeError):
            return {}
    
    def get_metrics_offsets(self):
        """Возвращает настройки смещения метрик"""
        try:
            return json.loads(self.metrics_offset_json)
        except (TypeError, json.JSONDecodeError):
            return {"recall_precision_offset": 0.0}
        

class CustomerFeaturesCurrent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    order_id = models.UUIDField()
    customer_unique_id = models.UUIDField()
    timeline_date = models.DateField()
    city_size = models.FloatField()
    city_center_distance_km = models.FloatField()
    city_center_level = models.FloatField()
    days_after_order = models.IntegerField()
    state_income = models.IntegerField()
    last_delivery_distance_km = models.IntegerField()
    last_delivery_cost = models.FloatField()
    last_order_cost = models.FloatField()
    last_review_score = models.IntegerField()
    last_review_length = models.IntegerField()
    last_review_product_state = models.IntegerField()
    last_review_sentiment = models.IntegerField()
    avg_order_interval_days = models.IntegerField()
    main_payment_type = models.CharField(max_length=250)
    last_order_day_of_year = models.IntegerField()
    # percent_null_reviews = models.FloatField()
    # dispersion_review_score
    # avg_review_message_length
    # product_count
    # order_date_variance
    # product_name_lenght
    # product_description_lenght
    # product_photos_qty
    pred_proba = models.FloatField()

    class Meta:
        verbose_name = 'Параметр прогнозирования'
        verbose_name_plural = 'Параметры прогнозирования'
        db_table = 'customer_features_current'
        managed = False

class CustomerAbcAnalysis(models.Model):
    customer_unique_id = models.CharField(
        max_length=255, 
        primary_key=True,  # Указываем что это PK вместо стандартного id
        db_column='customer_unique_id'
    )
    sum = models.DecimalField(max_digits=12, decimal_places=2)
    cumulative_revenue = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        db_column='"Cumulative revenue"'
    )
    cumulative_percentage = models.DecimalField(
        max_digits=9,
        decimal_places=7,
        db_column='"Cumulative percentage"'
    )
    category = models.CharField(
        max_length=1,
        db_column='"Category"'
    )
    class Meta:
        verbose_name = 'ABC анализ'
        verbose_name_plural = 'ABC анализы'
        db_table = 'analysis_abc_customer_payment_value'
        managed = False

