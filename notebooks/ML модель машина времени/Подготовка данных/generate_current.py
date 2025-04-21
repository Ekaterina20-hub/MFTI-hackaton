# Клиентов, у которых один заказ позднее чем минус 3 месяца от конца придётся выкинуть.
# Мы не можем однозначно сказать вернулись они или нет.
# Скрипт генерации дат для обработки тоже должен это учитывать даже если заказов много
# Естественно заказы после линии наблюдений используются для получения таргета, но не признаков

# Далее охуенный план:
# 1. Извлекаем всех клиентов
# 2. Идём циклом по каждому клиенту
# 3. Получаем для него все его ордера
# 4. Получаем все его отзывы
# 5. Формируем список дней, которые будут записаны в датасет
# Для клиентов у которых всего один заказ, это будет один случайный день между заказом и TIMELINE_FINISH_DATE
# У нас очень много одиночных заказов, по этому вероятно такой подробности должно хватить для модели
# Если заказов у клиента много, то для каждого интервала между заказами и TIMELINE_FINISH_DATE будет взято по неколько дней
# 6. Идём циклом по дням. Текущий день будет в timeline_date

import random
import datetime
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sources_db2 import connectDB

# Мы не будем учиться на ордерах позднее чем за 3 месяца до конца статистики,
# потому что там мы не можем уверенно сказать ушёл клиент или нет
# TIMELINE_FINISH_DATE = datetime.date(2018, 7, 31)# - datetime.timedelta(days=90)
TIMELINE_FINISH_DATE = datetime.date(2018, 8, 1)# - datetime.timedelta(days=90)
print(f'Финишная дата для признаков: {TIMELINE_FINISH_DATE}')

# TODO: перенести в хелпер
def get_random_day(start_date, end_date):
    days_between_dates = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between_dates) + 1
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def get_dates_itervals(dates):
    intervals = []
    intervals_count = len(dates)
    for i in range(intervals_count):
        start_date = dates[i]
        end_date = dates[i + 1] if i + 1 < intervals_count else TIMELINE_FINISH_DATE
        intervals.append((start_date, end_date))
    return intervals

def interval_days_needed(start_date, end_date):
    days = (end_date - start_date).days
    if days <= 3:
        return 1
    if days > 3 and days <= 7:
        return 2
        # return 3
    elif days > 7 and days <= 30:
        return 4
        # return 7
    return 6
    # return 15

def get_timeline_days(dates):
    global TIMELINE_FINISH_DATE
    dates = [x for x in dates if x < TIMELINE_FINISH_DATE]
    if not len(dates):
        print(f'Должна быть хотя бы одна дата, хотя бы один ордер до {TIMELINE_FINISH_DATE}')
        return []
    elif len(dates) == 1:
        start_date = dates[0]
        if start_date >= TIMELINE_FINISH_DATE:
            # Не интересуют даты позднее линии наблюдения
            return []
        return [get_random_day(start_date, TIMELINE_FINISH_DATE)]
    result = []
    intervals = get_dates_itervals(dates)
    for interval in intervals:
        items = []
        start_date = interval[0]
        end_date = interval[1]
        items_needed = interval_days_needed(start_date, end_date)
        fuse_counter = 0
        while fuse_counter < 10 and len(items) < items_needed:
            fuse_counter += 1
            day = get_random_day(start_date, end_date)
            if day not in items:
                items.append(day)
        result.extend(items)
    return result

def get_last_past_order(orders_df, timeline_date):
    past_orders = orders_df[orders_df['date_created'] < timeline_date]
    if not past_orders.empty:
        return past_orders.sort_values(by='date_created', ascending=False).iloc[0]
    else:
        return None

def get_nearest_future_order(orders_df, timeline_date):
    future_orders = orders_df[orders_df['date_created'] > timeline_date]
    if not future_orders.empty:
        return future_orders.sort_values(by='date_created', ascending=True).iloc[0]
    else:
        return None

def get_last_order_review(reviews_df, order_id):
    future_reviews = reviews_df[reviews_df['order_id'] == order_id]
    if not future_reviews.empty:
        return future_reviews.sort_values(by='date_created', ascending=False).iloc[0]
    else:
        return None

# database = connectDB("postgresql://hakaton_admin:fyT6r5Kd94Nko4d@94.142.142.59:5432/hakaton2_db")
database = connectDB("postgresql://anketa_admin:f4uh4uhu34fuy34fd@localhost:5432/hakaton2_db")

customer_index = 0

with database.connect() as connection:
    create_table_sql = text("""
    drop table if exists customer_features_current;
    CREATE TABLE if not exists customer_features_current (
        id SERIAL PRIMARY KEY, -- Уникальный идентификатор записи
        timeline_date DATE, -- Дата расчёта параметров. Идём день за днём.
        order_id UUID, -- Уникальный идентификатор ордера
        customer_unique_id UUID, -- Уникальный идентификатор клиента
        customer_state TEXT, -- Штат клиента
        customer_city TEXT, -- Город клиента
        city_size REAL, -- Размер города
        city_center_distance_km REAL, -- Расстояние от центра города в км
        city_center_level REAL, -- Расстояние от центра города
        days_after_order INT, -- Сколько прошло дней с последнего заказа
        days_before_order INT, -- ТАРГЕТ. Сколько осталось дней до следующего заказа
        is_customer_will_order boolean, -- ТАРГЕТ. Он ещё будет покупать в будущем?
        state_density REAL, -- Плотность населения по штату
        state_income REAL, -- Средний доход по штату
        state_north_south_index INT, -- Северный или южный штат. 0 - юг, 9 - север.
        last_delivery_distance_km REAL, -- Последний заказ: расстояние между продавцом и покупателем
        last_delivery_delay_days INT, -- Последний заказ: количество дней задержки
        last_delivery_cost REAL, -- Последний заказ: цена доставки
        last_order_cost REAL, -- Последний заказ: цена ордера
        last_cancelled boolean, -- Последний заказ: ордер был отменён
        last_delivered boolean, -- Последний заказ: заказ доставлен
        last_review_score INT, -- Последний отзыв: оценка клиента
        last_review_length INT, -- Последний отзыв: длина коментария в символах
        last_review_match_description boolean, -- Последний отзыв: товар соответствует описанию?
        last_review_product_state INT, -- Последний отзыв: состояние товара
        last_review_recommend boolean, -- Последний отзыв: клиент порекомендует сервис?
        last_review_sentiment INT, -- Последний отзыв: какое настроение клиента от -2 до 2?
        last_review_buy_again boolean, -- Последний отзыв: клиент обещает покупать снова?
        last_review_want_leave boolean, -- Последний отзыв: клиент угрожает уйти?
        last_review_unexpected_issues boolean, -- Последний отзыв: были неожиданные проблемы?
        last_review_quality_happy boolean, -- Последний отзыв: доволен качеством?
        avg_order_interval_days INT, -- Средний интервал между заказами
        main_payment_type TEXT, -- Предпочитаемый способ оплаты
        last_product_rating_min REAL, -- Последний заказ: средний рейтинг худшего товара
        last_product_rating_max REAL, -- Последний заказ: средний рейтинг лудшего товара
        last_product_size_max TEXT, -- Размер продукта максимальный
        last_product_weight_max REAL, -- Вес продукта максимальный
        last_product_name_lenght INT,
        last_product_description_lenght INT,
        last_product_photos_qty INT,
        first_product_abc REAL, -- ABC категория, первый купленный товар
        first_product_xyz REAL, -- XYZ категория, первый купленный товар
        last_product_abc REAL, -- ABC категория, последний купленный товар A = 1, B = 2, C = 3
        last_product_xyz REAL, -- XYZ категория, последний купленный товар X = 1, Y = 2, Z = 3
        last_order_month INT, -- Месяц последнего заказа
        last_order_day_of_year INT, -- Номер дня в году последнего заказа
        seller_orders_min INT, -- Продавец: общее количество ордеров у самого скромного продавца
        seller_repeat_rate_min REAL, -- Продавец: доля повторных покупок у худшего продавца
        seller_repeat_rate_max REAL, -- Продавец: доля повторных покупок у лучшего продавца
        seller_cancel_rate_min REAL, -- Продавец: доля отменённых заказов у худшего продавца
        rfm_score TEXT -- RFM клиента
    );
alter table customer_features_current add column pred_class bool null;
alter table customer_features_current add column pred_proba real null;
alter table customer_features_current add column shap_importances varchar null;""")
    connection.execute(create_table_sql)
    connection.commit()

customers = pd.read_sql_query(f"""SELECT * FROM analysis_geo_customers c""", database).to_dict('records')
# customers = pd.read_sql_query(f"""SELECT * FROM analysis_geo_customers c where orders_total=2;""", database).to_dict('records')
# customer = customers[2]
for customer in customers:
    customer_unique_id = customer['customer_unique_id']
    print('customer_unique_id', customer_unique_id)
    orders_df = pd.read_sql_query(f"""SELECT ago.*,
                                    agc.geolocation_radius_km,
                                    agc.name as customer_city,
                                    ags.population_density as state_density,
                                    ags.avg_income as state_income,
                                    ags.north_south_index as state_north_south_index
                                FROM analysis_geo_orders ago
                                left join analysis_geo_cities agc on agc.id = ago.customer_city_id
                                left join analysis_geo_states ags on ags.code = ago.customer_state_code
                                where ago.customer_unique_id='{customer_unique_id}' and ago.date_created < '{TIMELINE_FINISH_DATE}';""", database)
    reviews_df = pd.read_sql_query(f"""SELECT *,
        creation_date as date_created,
        length(message) as review_length
        FROM analysis_nlp_reviews anr where customer_unique_id='{customer_unique_id}';""", database)
    order_dates = list(set(orders_df['date_created'].to_list()))
    order_dates.sort()
    # timeline_dates = get_timeline_days(order_dates)
    # if TIMELINE_FINISH_DATE not in timeline_dates and len(timeline_dates):
    #     timeline_dates.append(TIMELINE_FINISH_DATE)
    # timeline_date = timeline_dates[0]
    timeline_date = TIMELINE_FINISH_DATE
    timeline_item = {}

    # 7. Получить последний предидущий перед timeline_date ордер
    # 7.1 Получить количество дней, прощедшее с момента создания последнего прошлого ордера
    # 7.2 Собираем всю доступную информацию по последнему ордеру
    # 7.3 Собираем всю доступную информацию по штату из последнего ордера (должно быть при leftjoinено)
    # 7.4 Собираем всю доступную информацию по городу из последнего ордера (должно быть при leftjoinено)
    last_previos_order = get_last_past_order(orders_df, timeline_date)
    if last_previos_order is None:
        print('customer_unique_id:', customer_unique_id)
        print(orders_df['order_id'])
        print(orders_df['date_created'])
        print(orders_df)
        print(timeline_date)
        continue
        raise Exception('Мы не могли оказаться до ордера и без. Это ошибка.')

    timeline_item['days_after_order'] = (timeline_date - last_previos_order['date_created']).days
    timeline_item['city_center_distance_km'] = last_previos_order['city_center_distance_km']
    timeline_item['city_center_level'] = last_previos_order['city_center_level']
    timeline_item['last_delivery_distance_km'] = last_previos_order['delivery_distance_km']
    timeline_item['last_delivery_delay_days'] = last_previos_order['delivery_delay']
    timeline_item['last_delivery_cost'] = last_previos_order['delivery_cost']
    timeline_item['last_order_cost'] = last_previos_order['order_cost']
    timeline_item['last_cancelled'] = last_previos_order['is_cancelled']
    timeline_item['last_delivered'] = last_previos_order['is_delivered']
    timeline_item['main_payment_type'] = last_previos_order['main_payment_type']
    timeline_item['city_size'] = last_previos_order['geolocation_radius_km']
    timeline_item['state_density'] = last_previos_order['state_density']
    timeline_item['state_income'] = last_previos_order['state_income']
    timeline_item['state_north_south_index'] = last_previos_order['state_north_south_index']
    timeline_item['last_order_month'] = timeline_date.month
    timeline_item['last_order_day_of_year'] = timeline_date.timetuple().tm_yday

    timeline_item['customer_state'] = last_previos_order['customer_state_code']
    timeline_item['timeline_date'] = timeline_date
    timeline_item['order_id'] = last_previos_order['order_id']
    timeline_item['customer_unique_id'] = last_previos_order['customer_unique_id']
    timeline_item['customer_city'] = last_previos_order['customer_city']

    # Считаем инревал покупок avg_order_interval_days
    timeline_item['avg_order_interval_days'] = 0
    previos_dates = [x for x in order_dates if x <=timeline_date]
    if len(previos_dates) > 1:
        intervals = get_dates_itervals(previos_dates)[:-1]
        intervals = [(x[1] - x[0]).days for x in intervals]
        timeline_item['avg_order_interval_days'] = np.mean(intervals)

    # 8. Получить ближайший последующий ордер, если такой есть
    # 8.2 Сколько дней осталось до последующего ордера?
    next_order = get_nearest_future_order(orders_df, timeline_date)
    timeline_item['days_before_order'] = (next_order['date_created'] - timeline_date).days if next_order is not None and next_order.any() else 10000
    # TODO: возможно вот тут стоит смотреть не есть ли вообще ордер впереди, а если он через 3 месяца
    timeline_item['is_customer_will_order'] = next_order is not None and next_order.any()

    # 9. Получаем последний отзыв до текущей даты, если есть и извлекаем все доступные данные
    # TODO: честно говоря возможно стоило бы смотреть на дату отзыва, если он привязан к этому ордеры. А так нам придётся надеятся на random.
    # Хм, так может нам тогда брать ревьювы не по дате, а по идентификатору ордера?
    # TODO: подумать над этим
    # Давай пока не по дате фильтровать отзывы, а по ордеру
    last_review = get_last_order_review(reviews_df, last_previos_order['order_id'])
    timeline_item['last_review_score'] = last_review['score'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_length'] = last_review['review_length'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_match_description'] = last_review['q1'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_product_state'] = last_review['q2'] if last_review is not None and last_review.any() and last_review['q2'] else 0
    timeline_item['last_review_recommend'] = last_review['q3'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_sentiment'] = last_review['q6'] if last_review is not None and last_review.any() and last_review['q6'] else 0
    timeline_item['last_review_buy_again'] = last_review['q7'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_want_leave'] = last_review['q8'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_unexpected_issues'] = last_review['q10'] if last_review is not None and last_review.any() else None
    timeline_item['last_review_quality_happy'] = last_review['q11'] if last_review is not None and last_review.any() else None

    # 10. Вставляем запись в БД
    insert_df = pd.DataFrame([timeline_item])
    # print(timeline_item)
    insert_df.to_sql('customer_features_current', database, if_exists='append', index=False)
