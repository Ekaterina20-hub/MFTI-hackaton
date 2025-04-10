import random
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Customer
from api.models import Product
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


# class CategorySerializer(serializers.ModelSerializer):

#     micon = serializers.SerializerMethodField(read_only=True)
#     childrens = serializers.SerializerMethodField(read_only=True)

#     def get_childrens(self, obj):
#         categories = Category.objects.filter(parent=obj)
#         serializers = CategorySerializer(categories, many=True)
#         return serializers.data

#     def get_micon(self, obj):
#         crop_options = {'size': (32, 32), 'crop': True}
#         try:
#             return get_thumbnailer(obj.icon).get_thumbnail(crop_options).url
#         except Exception as e:
#             pass

#     class Meta:
#         model = Category
#         fields = (
#             'id',
#             'title',
#             'icon',
#             'micon',
#             'childrens',
#         )

