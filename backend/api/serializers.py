import random
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Customer
from api.models import Product
from api.models import Review
from api.models import MLModel
from api.models import CustomerAbcAnalysis
from hackathon.sources_db import runQuery
# from easy_thumbnails.files import get_thumbnailer

class CustomerSerializer(serializers.ModelSerializer):
    
    fullname = serializers.SerializerMethodField(read_only=True)

    def get_fullname(self, obj):
        names =['Силва Сантос', 'Оливейра Коста', 'Перейра Роша', 'Алмейда Соуза', 'Карвалью Лима', 'Родригес Феррейра', 'Насименто Мартинс', 'Андраде Силвейра', 'Батиста Мораес', 'Кастро Рибейро', 'Гомес Корреа', 'Нунес да Силва', 'Фрейтас Паэс', 'Сампайо Азеведо', 'Барбоза Кавальканте', 'Машадо Толедо', 'Виейра Мело', 'Фигейредо Варгас', 'Симоэс Камоэс', 'Валенте Гонсалвес', 'Дуарте Пессоа', 'Фонсека Кунья', 'Бесерра Абреу', 'Гальярдо Пачеко', 'Лукези Алвес', 'Резенде Матос', 'Салес Сальгадо', 'Тейшейра Луз', 'Варгас Моура', 'Зампиери Паула', 'Араужу Кампос', 'Браганса Флорес', 'Каэтано Маседо', 'Домингес Мадейра', 'Эскобар Са да Коста', 'Фалкао Бевилаква', 'Гама Каэтано', 'Итапуа Жезус', 'Жулиао Албукерке', 'Калдас Дос Сантос', 'Ласерда Монтейро', 'Магальяес Д’Авила', 'Ногейра Серкейра', 'Пальярес де Андраде', 'Куинтанилья Сампайо', 'Рабело Валенса', 'Сампайо Медейрос', 'Таварес де Оливейра', 'Умбелйно Лима', 'Вилариньо Паэс', 'Шавьер Де Карвалью', 'Янкоски Перейра', 'Заваттини да Силва', 'Абреу Родригес', 'Беневенуто Феррейра', 'Камара Мартинс', 'Даллаго Насименто', 'Эспиндола Андраде', 'Фумагалли Батиста', 'Гранадос Кастро', 'Ирасабал Гомес', 'Жокис Нунес', 'Куарисма Фрейтас', 'Лискано Сампайо', 'Миранда Барбоза', 'Отавио Машадо', 'Пуйол Виейра', 'Калдейра Фигейредо', 'Салгеиро Симоэс', 'Тинео Валенте', 'Вергара Дуарте', 'Шагас Фонсека', 'Элияс Бесерра', 'Фаустино Гальярдо', 'Гарсия Лукези', 'Исаак Резенде', 'Жеронимо Салес', 'Леал Тейшейра', 'Москера Варгас', 'Нунс Зампиери', 'Орельяна Араужу', 'Перигоса Браганса', 'Куеироз Каэтано', 'Рего Домингес', 'Саградо Эскобар', 'Тибау Фалкао', 'Уркиза Гама', 'Васконселос Итапуа', 'Ксавьер Жулиао', 'Занкети Калдас', 'Акунья Ласерда', 'Бенедетти Магальяес', 'Куадрадо Ногейра', 'Дорадо Пальярес', 'Эстрада Куинтанилья', 'Фаркас Рабело', 'Гальяни Сампайо', 'Итало Таварес', 'Жименез Умбелйно', 'Корреа Вилариньо']
        return names[random.randint(0, len(names) - 1)]

    class Meta:
        model = Customer
        fields = (
            'id',
            'fullname',
            'customer_unique_id',
            'state_code',
            'city_id',
            'orders_total',
            'last_activity'
        )


class CustomerAbcAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAbcAnalysis
        fields = (
            'customer_unique_id',
            'sum',
            'cumulative_revenue',
            'cumulative_percentage',
            'category'
        )


class CustomerDetailSerializer(CustomerSerializer):
    abc_analysis = serializers.SerializerMethodField(read_only=True)
    products = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    
    def get_abc_analysis(self, obj):
        abc = CustomerAbcAnalysis.objects.filter(customer_unique_id=obj.customer_unique_id.hex).first()
        return CustomerAbcAnalysisSerializer(abc, many=False).data

    def get_products(self, obj):
        products_dict = runQuery(f'''
select oi.product_id from orders_items_clear oi 
left join orders o on o.order_id = oi.order_id
left join customers c on c.customer_id = o.customer_id
where c.customer_unique_id='{obj.customer_unique_id.hex}'
''')
        product_ids = [p['product_id'] for p in products_dict]
        products = Product.objects.filter(product_id__in = product_ids).all()
        return ProductSerializer(products, many=True).data

    def get_reviews(self, obj):
        reviews = Review.objects.filter(customer_unique_id=obj.customer_unique_id).all()
        return ReviewLightSerializer(reviews, many=True).data

    class Meta(CustomerSerializer.Meta):
        fields = CustomerSerializer.Meta.fields + (
            'abc_analysis',
            'products',
            'reviews',
        )


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            'product_id',
            'product_category_name',
            'product_name_lenght',
            'product_description_lenght',
            'product_photos_qty',
            'product_weight_g',
            'product_length_cm',
            'product_height_cm',
            'product_width_cm',
        )


class ReviewSerializer(serializers.ModelSerializer):
    
    customer = serializers.SerializerMethodField(read_only=True)

    def get_customer(self, obj):
        # TODO: добавить нормальную связь по ключу
        customer = Customer.objects.filter(customer_unique_id=obj.customer_unique_id).first()
        return CustomerSerializer(customer, many=False).data

    class Meta:
        model = Review
        fields = (
            'review_id',
            'order_id',
            'score',
            'message',
            'message_ru',
            'creation_date',
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
            'q8',
            'q9',
            'q10',
            'q11',
            'customer_unique_id',
            'customer',
        )


class ReviewLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'review_id',
            'order_id',
            'score',
            'message',
            'message_ru',
            'creation_date',
            'q2',
            'q6',
            'customer_unique_id',
        )


class MLModelSerializer(serializers.ModelSerializer):
    
    metrics_offset = serializers.SerializerMethodField(read_only=True)

    def get_metrics_offset(self, obj):
        return obj.metrics_offset_json

    class Meta:
        model = MLModel
        fields = (
            'name',
            'model_file',
            'feature_columns',
            # 'mean_values_json',
            # 'metrics_offset_json',
            'metrics_offset',
            'precision_true',
            'recall_true',
            'f1_true',
            'precision_false',
            'is_active',
            'is_main',
        )


class MLModelLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = MLModel
        fields = (
            'name',
            # 'feature_columns',
            'precision_true',
            'recall_true',
            'f1_true',
            'precision_false',
            'is_active',
            'is_main',
        )
